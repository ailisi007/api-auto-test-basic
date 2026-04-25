import logging

# 导入接口和测试数据
from api.post_api import get_post_list, add_post, update_post, delete_post
from data.test_data import test_data


# 执行完整流程：查询、新增、修改、删除
def test_post_flow(title, body):
    try:
        logging.info("---------- 开始本轮业务流程 ----------")

        # 先查一下列表
        get_post_list()

        # 新增帖子，拿到ID
        new_post = add_post(title=title, body=body)
        new_post_id = new_post["id"]

        # 用新增的ID去修改
        update_post(new_post_id, f"修改后的：{title}")

        # 再删除这个帖子
        delete_post(new_post_id)

        logging.info("---------- 本轮业务流程全部执行成功 ----------\n")

    except Exception as e:
        logging.error(f"❌ 本轮业务流程执行失败：{e}", exc_info=True)


# 主函数，循环跑用例
if __name__ == "__main__":
    # 循环执行所有数据
    for index, data in enumerate(test_data):
        logging.info(f"========== 第 {index + 1} 条参数化用例 ==========")
        
        # 取出数据
        title = data["title"]
        body = data["body"]
        
        # 开始执行流程
        test_post_flow(title, body)