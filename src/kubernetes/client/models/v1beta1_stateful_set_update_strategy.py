# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1StatefulSetUpdateStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rolling_update=None, type=None):
        """
        V1beta1StatefulSetUpdateStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rolling_update': 'V1beta1RollingUpdateStatefulSetStrategy',
            'type': 'str'
        }

        self.attribute_map = {
            'rolling_update': 'rollingUpdate',
            'type': 'type'
        }

        self._rolling_update = rolling_update
        self._type = type

    @property
    def rolling_update(self):
        """
        Gets the rolling_update of this V1beta1StatefulSetUpdateStrategy.
        RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.

        :return: The rolling_update of this V1beta1StatefulSetUpdateStrategy.
        :rtype: V1beta1RollingUpdateStatefulSetStrategy
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        """
        Sets the rolling_update of this V1beta1StatefulSetUpdateStrategy.
        RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.

        :param rolling_update: The rolling_update of this V1beta1StatefulSetUpdateStrategy.
        :type: V1beta1RollingUpdateStatefulSetStrategy
        """

        self._rolling_update = rolling_update

    @property
    def type(self):
        """
        Gets the type of this V1beta1StatefulSetUpdateStrategy.
        Type indicates the type of the StatefulSetUpdateStrategy.

        :return: The type of this V1beta1StatefulSetUpdateStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1beta1StatefulSetUpdateStrategy.
        Type indicates the type of the StatefulSetUpdateStrategy.

        :param type: The type of this V1beta1StatefulSetUpdateStrategy.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1StatefulSetUpdateStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
