# -*- coding: utf-8 -*-
from crawlfrontier.worker.server import JsonRpcResource, RootResource, JsonRpcError, jsonrpc_result, JsonRpcService


class TopicalSpiderResource(JsonRpcResource):

    def __init__(self, spider):
        self.spider = spider

    def process_request(self, method, jrequest):
        if method == 'configure':
            self.spider.configure(jrequest['job_config'])
            return jsonrpc_result(jrequest['id'], "success")
        raise JsonRpcError(400, "Unknown method")


class TopicalSpiderWebService(JsonRpcService):
    def __init__(self, spider, settings):
        root = RootResource()
        root.putChild('jsonrpc', TopicalSpiderResource(spider))
        JsonRpcService.__init__(self, root, settings)
        self.spider = spider

    def start_listening(self):
        JsonRpcService.start_listening(self)
        address = self.port.getHost()
        self.spider.set_process_info("%s:%d" % (address.host, address.port))