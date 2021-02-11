    def list_namespaced_cronjobs(self, namespace, **kwargs):  # noqa: E501
 
        kwargs['_return_http_data_only'] = True
        return self.list_namespaced_cronjobs_with_http_info(namespace, **kwargs)  # noqa: E501

    def list_namespaced_cronjobs_with_http_info(self, namespace, **kwargs):  # noqa: E501

        local_var_params = locals()

        all_params = [
            'namespace',
            'pretty',
            'allow_watch_bookmarks',
            '_continue',
            'field_selector',
            'label_selector',
            'limit',
            'resource_version',
            'timeout_seconds',
            'watch'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_namespaced_cronjobs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `list_namespaced_cronjobs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'allow_watch_bookmarks' in local_var_params and local_var_params['allow_watch_bookmarks'] is not None:  # noqa: E501
            query_params.append(('allowWatchBookmarks', local_var_params['allow_watch_bookmarks']))  # noqa: E501
        if '_continue' in local_var_params and local_var_params['_continue'] is not None:  # noqa: E501
            query_params.append(('continue', local_var_params['_continue']))  # noqa: E501
        if 'field_selector' in local_var_params and local_var_params['field_selector'] is not None:  # noqa: E501
            query_params.append(('fieldSelector', local_var_params['field_selector']))  # noqa: E501
        if 'label_selector' in local_var_params and local_var_params['label_selector'] is not None:  # noqa: E501
            query_params.append(('labelSelector', local_var_params['label_selector']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'resource_version' in local_var_params and local_var_params['resource_version'] is not None:  # noqa: E501
            query_params.append(('resourceVersion', local_var_params['resource_version']))  # noqa: E501
        if 'timeout_seconds' in local_var_params and local_var_params['timeout_seconds'] is not None:  # noqa: E501
            query_params.append(('timeoutSeconds', local_var_params['timeout_seconds']))  # noqa: E501
        if 'watch' in local_var_params and local_var_params['watch'] is not None:  # noqa: E501
            query_params.append(('watch', local_var_params['watch']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream=watch', 'application/vnd.kubernetes.protobuf;stream=watch'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/namespaces/{namespace}/cronjobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1CronjobList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)		
			
			
