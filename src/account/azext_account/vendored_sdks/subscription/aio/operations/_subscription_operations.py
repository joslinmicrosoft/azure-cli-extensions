# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._subscription_operations import (
    build_accept_ownership_request,
    build_accept_ownership_status_request,
    build_cancel_request,
    build_enable_request,
    build_rename_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SubscriptionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.subscription.aio.SubscriptionClient`'s
        :attr:`subscription` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def cancel(self, subscription_id: str, **kwargs: Any) -> _models.CanceledSubscriptionId:
        """The operation to cancel a subscription.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CanceledSubscriptionId or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.CanceledSubscriptionId
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CanceledSubscriptionId]

        request = build_cancel_request(
            subscription_id=subscription_id,
            api_version=api_version,
            template_url=self.cancel.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CanceledSubscriptionId", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    cancel.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel"}  # type: ignore

    @overload
    async def rename(
        self,
        subscription_id: str,
        body: _models.SubscriptionName,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RenamedSubscriptionId:
        """The operation to rename a subscription.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Subscription Name. Required.
        :type body: ~azure.mgmt.subscription.models.SubscriptionName
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenamedSubscriptionId or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.RenamedSubscriptionId
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def rename(
        self, subscription_id: str, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RenamedSubscriptionId:
        """The operation to rename a subscription.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Subscription Name. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenamedSubscriptionId or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.RenamedSubscriptionId
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def rename(
        self, subscription_id: str, body: Union[_models.SubscriptionName, IO], **kwargs: Any
    ) -> _models.RenamedSubscriptionId:
        """The operation to rename a subscription.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Subscription Name. Is either a model type or a IO type. Required.
        :type body: ~azure.mgmt.subscription.models.SubscriptionName or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenamedSubscriptionId or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.RenamedSubscriptionId
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RenamedSubscriptionId]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "SubscriptionName")

        request = build_rename_request(
            subscription_id=subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.rename.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RenamedSubscriptionId", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    rename.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename"}  # type: ignore

    @distributed_trace_async
    async def enable(self, subscription_id: str, **kwargs: Any) -> _models.EnabledSubscriptionId:
        """The operation to enable a subscription.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EnabledSubscriptionId or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.EnabledSubscriptionId
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.EnabledSubscriptionId]

        request = build_enable_request(
            subscription_id=subscription_id,
            api_version=api_version,
            template_url=self.enable.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("EnabledSubscriptionId", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    enable.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable"}  # type: ignore

    async def _accept_ownership_initial(  # pylint: disable=inconsistent-return-statements
        self, subscription_id: str, body: Union[_models.AcceptOwnershipRequest, IO], **kwargs: Any
    ) -> None:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "AcceptOwnershipRequest")

        request = build_accept_ownership_request(
            subscription_id=subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._accept_ownership_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _accept_ownership_initial.metadata = {"url": "/providers/Microsoft.Subscription/subscriptions/{subscriptionId}/acceptOwnership"}  # type: ignore

    @overload
    async def begin_accept_ownership(
        self,
        subscription_id: str,
        body: _models.AcceptOwnershipRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Accept subscription ownership.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Required.
        :type body: ~azure.mgmt.subscription.models.AcceptOwnershipRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_accept_ownership(
        self, subscription_id: str, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Accept subscription ownership.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_accept_ownership(
        self, subscription_id: str, body: Union[_models.AcceptOwnershipRequest, IO], **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Accept subscription ownership.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :param body: Is either a model type or a IO type. Required.
        :type body: ~azure.mgmt.subscription.models.AcceptOwnershipRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._accept_ownership_initial(  # type: ignore
                subscription_id=subscription_id,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_accept_ownership.metadata = {"url": "/providers/Microsoft.Subscription/subscriptions/{subscriptionId}/acceptOwnership"}  # type: ignore

    @distributed_trace_async
    async def accept_ownership_status(
        self, subscription_id: str, **kwargs: Any
    ) -> _models.AcceptOwnershipStatusResponse:
        """Accept subscription ownership status.

        :param subscription_id: Subscription Id. Required.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AcceptOwnershipStatusResponse or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.AcceptOwnershipStatusResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AcceptOwnershipStatusResponse]

        request = build_accept_ownership_status_request(
            subscription_id=subscription_id,
            api_version=api_version,
            template_url=self.accept_ownership_status.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AcceptOwnershipStatusResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    accept_ownership_status.metadata = {"url": "/providers/Microsoft.Subscription/subscriptions/{subscriptionId}/acceptOwnershipStatus"}  # type: ignore
