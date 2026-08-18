from architecture.api.rest.v2.common.base.api_base import Api
from architecture.api.rest.v2.common.server import Server

class ApiV2(Api):
    def __init__(self):
        super().__init__()
        server = Server()
        self.base_url = server.get_base_url()

# if __name__ == '__main__':
#     api_v2 = ApiV2()
#     # print([p.joinpath('test_bed.yaml') for p in Path(__file__).resolve().parents if p.joinpath('test_bed.yaml').is_file()][0])
#     print(api_v2.base_url)