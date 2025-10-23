import database

if __name__ == '__main__':
    sy = database.SiYuan(sy_ip="127.0.0.1", sy_port="6806",sy_token="g8dpu94hb1oaujuj")
    db = database.DataBase(sy=sy, av_id="20251022141749-fmw1vuj")
    data = db.getAttributeViewKeys()
    dbb1 = database.DataBaseBlocks()
    for x in data["data"]:
        type = x["type"]
        name = x["name"]
        key_id = x["id"]
        if type == "block":
            dbb1.setBlock(key_id, "test_block")
        elif type == "text":
            dbb1.setText(key_id, "test_text")
        elif type == "number":
            dbb1.setNumber(key_id, 1234.01)
        elif type == "select":
            dbb1.setSelect(key_id, "one", "1")
        elif type == "mSelect":
            dbb1.setmSelect(key_id, ["one","two"], ["1","2"])
        elif type == "date":
            dbb1.setDate(key_id, 1761188880000)
        elif type == "mAsset":
            dbb1.setmAsset(key_id, ["file"],[""],["www.baidu.com"])
        elif type == "checkbox":
            dbb1.setCheckbox(key_id, True)
        elif type == "url":
            dbb1.setUrl(key_id, "www.baidu.com")
        elif type == "email":
            dbb1.setEmail(key_id, "12345678@qq.com")
        elif type == "phone":
            dbb1.setPhone(key_id, "12345678")
        print(type, name, key_id)
    block_values = dbb1.getBlocksValues()
    print(block_values)
    ret = db.appendAttributeViewDetachedBlocksWithValues(block_values)
    print(ret)
    #dbb1.setBlock("")
    print(data)
