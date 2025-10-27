import json
import requests
from urllib.parse import urljoin

class SiYuan():
    def __init__(self, sy_ip:str, sy_port:str, sy_token:str) -> None:
        self.url = f"http://{sy_ip}:{sy_port}"
        self.token = sy_token
        self.headers = {"Authorization":f"Token {sy_token}"}

class DataBaseBlocks():
    def __init__(self) -> None:
        self.__blocks_values = []

    def setBlock(self, key_id: str, content: str):
        """
        设置主键字段

        Args:
            key_id: str，字段ID
            content: str, 主键字段内容

        Returns:
            None

        Example:
            setBlock("20251023173304-ccy7ec9", "test_block")
        """
        value = {
            "keyID": key_id,
            "block": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setText(self, key_id: str, content: str):
        """
        设置文本字段

        Args:
            key_id: str，字段ID
            content: str, 文本字段内容

        Returns:
            None

        Example:
            setText("20251023173304-ccy7ec9", "test_text")
        """
        value = {
            "keyID": key_id,
            "text": {
                "content": content
            }
        }
        self.__blocks_values.append(value)
    def setSelect(self, key_id: str, content: str, color: str):
        """
        设置单选字段

        Args:
            key_id: str，字段ID
            content: str, 单选字段内容
            color: str, [0~14]单选字段颜色

        Returns:
            None

        Example:
            setSelect("20251023173304-ccy7ec9", "test_select", "1")
        """
        value = {
            "keyID": key_id,
            "mSelect": [{
                "content": content,
                "color": color
            }]
        }
        self.__blocks_values.append(value)
    def setmSelect(self, key_id: str, contents: list, colors: list):
        """
        设置单选字段

        Args:
            key_id: str，字段ID
            contents: list, 单选字段内容列表
            colors: list, [0~14]单选字段颜色列表

        Returns:
            None

        Example:
            setSelect("20251023173304-ccy7ec9", ["one", "two"], ["1", "2"])
        """
        value = {
            "keyID": key_id,
            "mSelect": []
        }
        if len(contents) != len(colors):
            raise "contents 和 colors 个数需要相同"
        for index, content in enumerate(contents):
            value["mSelect"].append(
                {
                    "content": content,
                    "color": colors[index]
                }
            )
        self.__blocks_values.append(value)

    def setDate(self, key_id: str, date: int,
                is_not_empty: bool = False,
                has_end_date: bool = False,
                is_not_time: bool = False):
        """
        设置日期字段

        Args:
            key_id: str，字段ID
            date: int, 设置时间戳
            is_not_empty: bool, 字段值是否为空
            has_end_date: bool, 是否有结束时间
            is_not_time: bool, 是否是具体时间

        Returns:
            None

        Example:
            setDate("20251023173304-ccy7ec9", 1761188880000)
        """
        value = {
            "keyID": key_id,
            "date": {
                "content": date,
                "isNotEmpty": is_not_empty,
                "hasEndDate": has_end_date,
                "isNotTime": is_not_time,
                "formattedContent": ""
            }
        }
        self.__blocks_values.append(value)

    def setmAsset(self, key_id: str, types: list, names: list, contents: list):
        """
        设置资源字段值

        Args:
            key_id: str，字段ID
            types: list, 资源类型列表[file (链接资源，文件资源), image(图片资源)]
            names: list, 资源名列表
            contents: list, 资源文本列表

        Returns:
            None

        Example:
            setmAsset("20251023173304-ccy7ec9", ["file"], [""], ["www.baidu.com"])
        """

        """ 插入资源字段值
        """
        value = {
            "keyID": key_id,
            "mAsset": []
        }
        lst = [len(types), len(names), len(contents)]
        if len(set(lst)) != 1:
            raise "参数个数不同"
        for index, type in enumerate(types):
            value["mAsset"].append({
                "type": type,
                "name": names[index],
                "content": contents[index]
            })
        self.__blocks_values.append(value)

    def setCheckbox(self, key_id: str, checked: bool):
        """
        设置复选框字段

        Args:
            key_id: str，字段ID
            checked: bool, 是否被选中 [False,True]

        Returns:
            None

        Example:
            setCheckbox("20251023173304-ccy7ec9", False)
        """
        value = {
            "keyID": key_id,
            "checkbox": {
                "checked": checked
            }
        }
        self.__blocks_values.append(value)
    
    def setUrl(self, key_id: str, content: str):
        """
        设置链接字段

        Args:
            key_id: str, 字段ID
            content: str, 链接内容

        Returns:
            None

        Example:
            setUrl("20251023173304-ccy7ec9", "www.baidu.com")
        """
        value = {
            "keyID": key_id,
            "url": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setEmail(self, key_id: str, content: str):
        """
        设置邮件字段

        Args:
            key_id: str, 字段ID
            content: str, 邮件内容

        Returns:
            None

        Example:
            setEmail("20251023173304-ccy7ec9", "12345678@qq.com")
        """

        value = {
            "keyID": key_id,
            "email": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setPhone(self, key_id: str, content: str):
        """
        设置电话字段

        Args:
            key_id: str, 字段ID
            content: str, 电话内容

        Returns:
            None

        Example:
            setPhone("20251023173304-ccy7ec9", "12345678")
        """
        value = {
            "keyID": key_id,
            "phone": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setTemplate(self, key_id: str, content: str):
        """
        设置模板字段

        Args:
            key_id: str, 字段ID
            content: str, 模板内容

        Returns:
            None

        Example:
            setTemplate("20251023173304-ccy7ec9","template")
        """
        value = {
            "keyID": key_id,
            "template": {
                "content": content
            }
        }
        self.__blocks_values.append(value)
    
    def setNumber(self, key_id: str, content: int):
        """
        设置数字字段

        Args:
            key_id: str, 字段ID
            content: int, 数字内容

        Returns:
            None

        Example:
            setTemplate("20251023173304-ccy7ec9", 123.00)
        """

        value = {
            "keyID": key_id,
            "number": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setRelation(self, key_id: str, content: str):
        """ 关联字段，TODO
        """
        value = {
            "keyID": key_id,
            "relation": {
                "content": content
            }
        }
        self.__blocks_values.append(value)

    def setRollUp(self, key_id: str, content: str):
        """ 汇总字段，TODO
        """
        value = {
            "keyID": key_id,
            "rollup": {
                "content": content
            }
        }
        self.__blocks_values.append(value)
    
    def getBlocksValues(self):
        """
        获取设置好的数据库字段值

        Args:
           None

        Returns:
            __blocks_values: 设置好的数据库字段值

        Example:
            blocks_values = getBlocksValues()
        """
        return self.__blocks_values
    
    def clearBlocksValues(self):
        """
        清空数据库字段值

        Args:
            None

        Returns:
            None

        Example:
           clearBlocksValues()
        """
        self.__blocks_values.clear()

class DataBase():
    def __init__(self, sy:SiYuan, av_id:str) -> None:
        self.url = sy.url
        self.headers = sy.headers
        self.av_id = av_id
        self.session = requests.session()

    def getAttributeViewKeys(self):
        """
        通过视图ID获取属性值

        Args:
            None

        Returns:
            字段属性JSON

        Example:
            getAttributeViewKeys():
        """
        url = urljoin(self.url, "api/av/getAttributeViewKeysByAvID")
        data = {
            "avID": self.av_id
        }
        res = self.session.post(url, headers=self.headers, json=data, timeout=5)
        res.raise_for_status()
        return json.loads(res.content)
    
    def getAttributeViewPrimaryKeyValues(self):
        """
        获取属性视图主键值

        Args:
            argument_name: type and description.

        Returns:
            type and description of the returned object.

        Example:
            # Description of my example.
            use_it_this_way(arg1, arg2)
        """
        pass

    def renderAttributeView(self, view_id: str, block_id: str, query: str, page_size: int = 50):
        """
        渲染数据库

        Args:
            view_id: str, 数据库视图ID
            block_id: str, 块ID
            query: str, 检索命令
            page_size: int, 默认50行数据，获取数据数量

        Returns:
            返回数据库视图中所有数据

        Example:
            renderAttributeView("20251022141749-fmw1vuj", "20251022141744-y6s3vtn", "", page_size=10)
        """
        url = urljoin(self.url, "api/av/renderAttributeView")
        data = {
            "id":self.av_id,
            "pageSize":page_size,
            "groupPaging":{},
            "viewID":view_id,
            "query":query,
            "blockID":block_id
        }
        res = self.session.post(url, headers=self.headers, json=data, timeout=5)
        res.raise_for_status()
        return json.loads(res.content)

    def appendAttributeViewDetachedBlocksWithValues(self, blocks_values: DataBaseBlocks):
        """
        在数据库中自动创建一行，并且添加值

        Args:
            blocks_values: DataBaseBlocks, 数据库添加数据，通过DataBaseBlocks类拼接

        Returns:
            返回状态

        Example:
            dbb1 = database.DataBaseBlocks()
            appendAttributeViewDetachedBlocksWithValues(dbb1.getBlocksValues())
        """

        """ 在数据库中自动创建一行，并且添加值
        """
        url = urljoin(self.url, "api/av/appendAttributeViewDetachedBlocksWithValues")
        data = {
            "avID": self.av_id,
            "blocksValues": [blocks_values]
        }
        res = self.session.post(url, headers=self.headers, json=data, timeout=5)
        res.raise_for_status()
        return json.loads(res.content)

