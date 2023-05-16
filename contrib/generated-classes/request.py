from typing import List
from typing import Type

from . import _base
from .obs_ratings import ObsRatings
from .request_action import RequestAction
from .request_state import RequestState


class Request(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['id', 'creator']
    _elements: List[str] = ['action', 'state', 'description', 'priority', 'review', 'history', 'title', 'accept_at']

    _id_is_optional: bool = True

    @property
    def id(self) -> str:
        return self._get_attribute("id")

    @id.setter
    def id(self, value: str):
        self._set_attribute("id", value)

    @id.deleter
    def id(self):
        self._delete_attribute("id")

    _creator_is_optional: bool = True

    @property
    def creator(self) -> str:
        return self._get_attribute("creator")

    @creator.setter
    def creator(self, value: str):
        self._set_attribute("creator", value)

    @creator.deleter
    def creator(self):
        self._delete_attribute("creator")
# {'list': '1+', 'ref': 'request-action-element'}

    _actions_is_list: bool = True
    _actions_wrapper_class: Type = RequestAction

    @property
    def actions(self) -> List[RequestAction]:
        return self._get_element("action", property_name="actions")

    @actions.setter
    def actions(self, value: List[RequestAction]):
        self._set_element("action", value, property_name="actions")

    @actions.deleter
    def actions(self):
        self._delete_element("action", property_name="actions")
# {'optional': '1', 'ref': 'request-state-element'}

    _state_wrapper_class: Type = RequestState
    _state_is_optional: bool = True

    @property
    def state(self) -> RequestState:
        return self._get_element("state")

    @state.setter
    def state(self, value: RequestState):
        self._set_element("state", value)

    @state.deleter
    def state(self):
        self._delete_element("state")
# {'optional': '1'}

    _description_is_optional: bool = True

    @property
    def description(self) -> str:
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'optional': '1', 'ref': 'obs-ratings'}

    _priority_wrapper_class: Type = ObsRatings
    _priority_is_optional: bool = True

    @property
    def priority(self) -> ObsRatings:
        return self._get_element("priority")

    @priority.setter
    def priority(self, value: ObsRatings):
        self._set_element("priority", value)

    @priority.deleter
    def priority(self):
        self._delete_element("priority")
# {'list': '0+', 'attributes': {'state': {'ref': 'request-states'}, 'by_user': {'optional': '1'}, 'by_group': {'optional': '1'}, 'by_project': {'optional': '1'}, 'by_package': {'optional': '1'}, 'who': {'optional': '1'}, 'when': {'optional': '1'}}, 'elements': {'comment': {'optional': '1'}, 'history': {'list': '0+', 'attributes': {'who': {}, 'when': {}}, 'elements': {'description': {}, 'comment': {'optional': '1'}}}}}

    _reviews_is_list: bool = True
    _reviews_attributes: List[str] = ['state', 'by_user', 'by_group', 'by_project', 'by_package', 'who', 'when']
    _reviews_elements: List[str] = ['comment', 'history']

    @property
    def reviews(self) -> List[str]:
        return self._get_element("review", property_name="reviews")

    @reviews.setter
    def reviews(self, value: List[str]):
        self._set_element("review", value, property_name="reviews")

    @reviews.deleter
    def reviews(self):
        self._delete_element("review", property_name="reviews")
# {'list': '0+', 'attributes': {'who': {}, 'when': {}}, 'elements': {'description': {}, 'comment': {'optional': '1'}}}

    _histories_is_list: bool = True
    _histories_attributes: List[str] = ['who', 'when']
    _histories_elements: List[str] = ['description', 'comment']

    @property
    def histories(self) -> List[str]:
        return self._get_element("history", property_name="histories")

    @histories.setter
    def histories(self, value: List[str]):
        self._set_element("history", value, property_name="histories")

    @histories.deleter
    def histories(self):
        self._delete_element("history", property_name="histories")
# {'optional': '1'}

    _title_is_optional: bool = True

    @property
    def title(self) -> str:
        return self._get_element("title")

    @title.setter
    def title(self, value: str):
        self._set_element("title", value)

    @title.deleter
    def title(self):
        self._delete_element("title")
# {'optional': '1'}

    _accept_at_is_optional: bool = True

    @property
    def accept_at(self) -> str:
        return self._get_element("accept_at")

    @accept_at.setter
    def accept_at(self, value: str):
        self._set_element("accept_at", value)

    @accept_at.deleter
    def accept_at(self):
        self._delete_element("accept_at")
