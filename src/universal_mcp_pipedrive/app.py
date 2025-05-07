from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class PipedriveApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='pipedrive', integration=integration, **kwargs)
        self.base_url = "https://api.pipedrive.com/v1"

    def oauth_request_authorization(self, client_id, redirect_uri, state=None) -> Any:
        """
        Redirects the user to an authorization server toassistant

        Redirects the user to an authorization server to obtain consent for a client application using the OAuth 2.0 protocol, with parameters for client identification and callback URI.

        Args:
            client_id (string): The client ID provided to you by the Pipedrive Marketplace when you register your app
            redirect_uri (string): The callback URL you provided when you registered your app. Authorization code will be sent to that URL (if it matches with the value you entered in the registration form) if a user approves the app install. Or, if a customer declines, the corresponding error will also be sent to this URL.
            state (string): You may pass any random string as the state parameter and the same string will be returned to your app after a user authorizes access. It may be used to store the user's session ID from your app or distinguish different responses. Using state may increase security; see RFC-6749. The state parameter is not automatically available in Marketplace Manager. To enable it for your app, please write to us at marketplace.devs@pipedrive.com.

        Returns:
            Any: Authorize user in the app.

        Tags:
            Oauth
        """
        url = f"{self.base_url}/oauth/authorize"
        query_params = {k: v for k, v in [('client_id', client_id), ('redirect_uri', redirect_uri), ('state', state)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()


    def activities_delete_bulk(self, ids) -> dict[str, Any]:
        """
        Deletes multiple activities by their IDs using query parameters and returns a success response upon completion.

        Args:
            ids (string): The comma-separated IDs of activities that will be deleted

        Returns:
            dict[str, Any]: The activities were successfully deleted

        Tags:
            Activities
        """
        url = f"{self.base_url}/activities"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_list_user_activities(self, user_id=None, filter_id=None, type=None, limit=None, start=None, start_date=None, end_date=None, done=None) -> dict[str, Any]:
        """
        Retrieves a list of activities filtered by user_id, type, date range, completion status, and other parameters.

        Args:
            user_id (integer): The ID of the user whose activities will be fetched. If omitted, the user associated with the API token will be used. If 0, activities for all company users will be fetched based on the permission sets.
            filter_id (integer): The ID of the filter to use (will narrow down results if used together with `user_id` parameter)
            type (string): The type of the activity, can be one type or multiple types separated by a comma. This is in correlation with the `key_string` parameter of ActivityTypes.
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Example: '100'.
            start (integer): For pagination, the position that represents the first result for the page Example: '0'.
            start_date (string): Use the activity due date where you wish to begin fetching activities from. Insert due date in YYYY-MM-DD format.
            end_date (string): Use the activity due date where you wish to stop fetching activities from. Insert due date in YYYY-MM-DD format.
            done (number): Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted returns both done and not done activities.

        Returns:
            dict[str, Any]: A list of activities

        Tags:
            Activities
        """
        url = f"{self.base_url}/activities"
        query_params = {k: v for k, v in [('user_id', user_id), ('filter_id', filter_id), ('type', type), ('limit', limit), ('start', start), ('start_date', start_date), ('end_date', end_date), ('done', done)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_add_new_activity(self, due_date=None, due_time=None, duration=None, deal_id=None, lead_id=None, person_id=None, project_id=None, org_id=None, location=None, public_description=None, note=None, subject=None, type=None, user_id=None, participants=None, busy_flag=None, attendees=None, done=None) -> dict[str, Any]:
        """
        Creates a new activity resource and returns a success status upon creation.

        Args:
            due_date (string): The due date of the activity. Format: YYYY-MM-DD
            due_time (string): The due time of the activity in UTC. Format: HH:MM
            duration (string): The duration of the activity. Format: HH:MM
            deal_id (integer): The ID of the deal this activity is associated with
            lead_id (string): The ID of the lead in the UUID format this activity is associated with
            person_id (integer): The ID of the person this activity is associated with
            project_id (integer): The ID of the project this activity is associated with
            org_id (integer): The ID of the organization this activity is associated with
            location (string): The address of the activity. Pipedrive will automatically check if the location matches a geo-location on Google maps.
            public_description (string): Additional details about the activity that is synced to your external calendar. Unlike the note added to the activity, the description is publicly visible to any guests added to the activity.
            note (string): The note of the activity (HTML format)
            subject (string): The subject of the activity. When value for subject is not set, it will be given a default value `Call`.
            type (string): The type of the activity. This is in correlation with the `key_string` parameter of ActivityTypes. When value for type is not set, it will be given a default value `Call`.
            user_id (integer): The ID of the user whom the activity is assigned to. If omitted, the activity is assigned to the authorized user.
            participants (array): List of multiple persons (participants) this activity is associated with. If omitted, single participant from `person_id` field is used. It requires a structure as follows: `[{"person_id":1,"primary_flag":true}]`
            busy_flag (boolean): Set the activity as 'Busy' or 'Free'. If the flag is set to `true`, your customers will not be able to book that time slot through any Scheduler links. The flag can also be unset by never setting it or overriding it with `null`. When the value of the flag is unset (`null`), the flag defaults to 'Busy' if it has a time set, and 'Free' if it is an all-day event without specified time.
            attendees (array): The attendees of the activity. This can be either your existing Pipedrive contacts or an external email address. It requires a structure as follows: `[{"email_address":"mail@example.org"}]` or `[{"person_id":1, "email_address":"mail@example.org"}]`
            done (string): Whether the activity is done or not. 0 = Not done, 1 = Done

        Returns:
            dict[str, Any]: Created

        Tags:
            Activities
        """
        request_body = {
            'due_date': due_date,
            'due_time': due_time,
            'duration': duration,
            'deal_id': deal_id,
            'lead_id': lead_id,
            'person_id': person_id,
            'project_id': project_id,
            'org_id': org_id,
            'location': location,
            'public_description': public_description,
            'note': note,
            'subject': subject,
            'type': type,
            'user_id': user_id,
            'participants': participants,
            'busy_flag': busy_flag,
            'attendees': attendees,
            'done': done,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/activities"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_get_all_activities(self, cursor=None, limit=None, since=None, until=None, user_id=None, done=None, type=None) -> dict[str, Any]:
        """
        Retrieves a paginated collection of activities filtered by parameters such as user, time range, completion status, and activity type.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed. Example: '100'.
            since (string): The time boundary that points to the start of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            until (string): The time boundary that points to the end of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            user_id (integer): The ID of the user whose activities will be fetched. If omitted, all activities are returned.
            done (boolean): Whether the activity is done or not. `false` = Not done, `true` = Done. If omitted, returns both done and not done activities.
            type (string): The type of the activity, can be one type or multiple types separated by a comma. This is in correlation with the `key_string` parameter of ActivityTypes.

        Returns:
            dict[str, Any]: A list of activities

        Tags:
            Activities
        """
        url = f"{self.base_url}/activities/collection"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('since', since), ('until', until), ('user_id', user_id), ('done', done), ('type', type)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes the specified activity by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: The activity was successfully deleted

        Tags:
            Activities
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/activities/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves details of an activity by its ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: The request was successful

        Tags:
            Activities
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/activities/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activities_update_activity_details(self, id, due_date=None, due_time=None, duration=None, deal_id=None, lead_id=None, person_id=None, project_id=None, org_id=None, location=None, public_description=None, note=None, subject=None, type=None, user_id=None, participants=None, busy_flag=None, attendees=None, done=None) -> dict[str, Any]:
        """
        Updates an existing activity specified by {id} and returns a success status upon completion.

        Args:
            id (string): id
            due_date (string): The due date of the activity. Format: YYYY-MM-DD
            due_time (string): The due time of the activity in UTC. Format: HH:MM
            duration (string): The duration of the activity. Format: HH:MM
            deal_id (integer): The ID of the deal this activity is associated with
            lead_id (string): The ID of the lead in the UUID format this activity is associated with
            person_id (integer): The ID of the person this activity is associated with
            project_id (integer): The ID of the project this activity is associated with
            org_id (integer): The ID of the organization this activity is associated with
            location (string): The address of the activity. Pipedrive will automatically check if the location matches a geo-location on Google maps.
            public_description (string): Additional details about the activity that is synced to your external calendar. Unlike the note added to the activity, the description is publicly visible to any guests added to the activity.
            note (string): The note of the activity (HTML format)
            subject (string): The subject of the activity
            type (string): The type of the activity. This is in correlation with the `key_string` parameter of ActivityTypes.
            user_id (integer): The ID of the user whom the activity is assigned to
            participants (array): List of multiple persons (participants) this activity is associated with. It requires a structure as follows: `[{"person_id":1,"primary_flag":true}]`
            busy_flag (boolean): Set the activity as 'Busy' or 'Free'. If the flag is set to `true`, your customers will not be able to book that time slot through any Scheduler links. The flag can also be unset by never setting it or overriding it with `null`. When the value of the flag is unset (`null`), the flag defaults to 'Busy' if it has a time set, and 'Free' if it is an all-day event without specified time.
            attendees (array): The attendees of the activity. This can be either your existing Pipedrive contacts or an external email address. It requires a structure as follows: `[{"email_address":"mail@example.org"}]` or `[{"person_id":1, "email_address":"mail@example.org"}]`
            done (string): Whether the activity is done or not. 0 = Not done, 1 = Done

        Returns:
            dict[str, Any]: The request was successful

        Tags:
            Activities
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'due_date': due_date,
            'due_time': due_time,
            'duration': duration,
            'deal_id': deal_id,
            'lead_id': lead_id,
            'person_id': person_id,
            'project_id': project_id,
            'org_id': org_id,
            'location': location,
            'public_description': public_description,
            'note': note,
            'subject': subject,
            'type': type,
            'user_id': user_id,
            'participants': participants,
            'busy_flag': busy_flag,
            'attendees': attendees,
            'done': done,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/activities/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_fields_get_all(self) -> Any:
        """
        Retrieves all activity fields from the Pipedrive API using the "GET" method at the path "/activityFields".

        Returns:
            Any: Success

        Tags:
            ActivityFields
        """
        url = f"{self.base_url}/activityFields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_types_mark_as_deleted_bulk(self, ids) -> Any:
        """
        Deletes specified activity types by IDs using their identifiers and returns a success status upon completion.

        Args:
            ids (string): The comma-separated activity type IDs

        Returns:
            Any: The activity types were successfully deleted

        Tags:
            ActivityTypes
        """
        url = f"{self.base_url}/activityTypes"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_types_list_all_activity_types(self) -> Any:
        """
        Retrieves a list of available activity types with their details from the Fitbit activity database.

        Returns:
            Any: A list of activity types

        Tags:
            ActivityTypes
        """
        url = f"{self.base_url}/activityTypes"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_types_add_new_type(self, name, icon_key, color=None) -> Any:
        """
        Creates a new activity type using the specified data and returns a success status upon completion.

        Args:
            name (string): The name of the activity type Example: 'call'.
            icon_key (string): Icon graphic to use for representing this activity type
            color (string): A designated color for the activity type in 6-character HEX format (e.g. `FFFFFF` for white, `000000` for black) Example: 'FFFFFF'.

        Returns:
            Any: The activity type was successfully created

        Tags:
            ActivityTypes
        """
        request_body = {
            'name': name,
            'icon_key': icon_key,
            'color': color,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/activityTypes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_types_mark_as_deleted(self, id) -> Any:
        """
        Deletes an activity type by its ID using the Pipedrive API.

        Args:
            id (string): id

        Returns:
            Any: The activity type was successfully deleted

        Tags:
            ActivityTypes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/activityTypes/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activity_types_update_type(self, id, name=None, icon_key=None, color=None, order_nr=None) -> Any:
        """
        Updates an existing activity type by modifying its details using the API and returns a successful response.

        Args:
            id (string): id
            name (string): The name of the activity type
            icon_key (string): Icon graphic to use for representing this activity type
            color (string): A designated color for the activity type in 6-character HEX format (e.g. `FFFFFF` for white, `000000` for black)
            order_nr (integer): An order number for this activity type. Order numbers should be used to order the types in the activity type selections.

        Returns:
            Any: The activity type was successfully updated

        Tags:
            ActivityTypes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'icon_key': icon_key,
            'color': color,
            'order_nr': order_nr,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/activityTypes/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def billing_get_addons_for_single_company(self) -> Any:
        """
        Retrieves available addons for billing subscriptions, returning a list of additional features or services that can be added to a subscription plan.

        Returns:
            Any: Success

        Tags:
            Billing
        """
        url = f"{self.base_url}/billing/subscriptions/addons"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_logs_add_new_log(self, outcome, to_phone_number, start_time, end_time, user_id=None, activity_id=None, subject=None, duration=None, from_phone_number=None, person_id=None, org_id=None, deal_id=None, lead_id=None, note=None) -> dict[str, Any]:
        """
        Logs API calls at the "/callLogs" endpoint via POST and returns HTTP status codes for operation results.

        Args:
            outcome (string): Describes the outcome of the call
            to_phone_number (string): The number called
            start_time (string): The date and time of the start of the call in UTC. Format: YYYY-MM-DD HH:MM:SS.
            end_time (string): The date and time of the end of the call in UTC. Format: YYYY-MM-DD HH:MM:SS.
            user_id (integer): The ID of the owner of the call log. Please note that a user without account settings access cannot create call logs for other users.
            activity_id (integer): If specified, this activity will be converted into a call log, with the information provided. When this field is used, you don't need to specify `deal_id`, `person_id` or `org_id`, as they will be ignored in favor of the values already available in the activity. The `activity_id` must refer to a `call` type activity.
            subject (string): The name of the activity this call is attached to
            duration (string): The duration of the call in seconds
            from_phone_number (string): The number that made the call
            person_id (integer): The ID of the person this call is associated with
            org_id (integer): The ID of the organization this call is associated with
            deal_id (integer): The ID of the deal this call is associated with. A call log can be associated with either a deal or a lead, but not both at once.
            lead_id (string): The ID of the lead in the UUID format this call is associated with. A call log can be associated with either a deal or a lead, but not both at once.
            note (string): The note for the call log in HTML format

        Returns:
            dict[str, Any]: The call log was successfully created.

        Tags:
            CallLogs
        """
        request_body = {
            'user_id': user_id,
            'activity_id': activity_id,
            'subject': subject,
            'duration': duration,
            'outcome': outcome,
            'from_phone_number': from_phone_number,
            'to_phone_number': to_phone_number,
            'start_time': start_time,
            'end_time': end_time,
            'person_id': person_id,
            'org_id': org_id,
            'deal_id': deal_id,
            'lead_id': lead_id,
            'note': note,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/callLogs"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_logs_get_all_logs(self, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of call logs based on specified query parameters, allowing users to view and manage call history by setting a start point and limiting the number of results returned.

        Args:
            start (integer): Pagination start
            limit (integer): For pagination, the limit of entries to be returned. The upper limit is 50.

        Returns:
            dict[str, Any]: A list of call logs.

        Tags:
            CallLogs
        """
        url = f"{self.base_url}/callLogs"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_logs_delete_log(self, id) -> dict[str, Any]:
        """
        Deletes a call log (including any attached audio recordings) without affecting related activities using the specified ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: The call log was successfully deleted.

        Tags:
            CallLogs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/callLogs/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def call_logs_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves a specific call log entry by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: The requested call log object.

        Tags:
            CallLogs
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/callLogs/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

   
    def channels_create_new_channel(self, name, provider_channel_id, avatar_url=None, template_support=False, provider_type="other") -> dict[str, Any]:
        """
        Creates a new channel resource and returns the operation status.

        Args:
            name (string): The name of the channel Example: 'My Channel'.
            provider_channel_id (string): The channel ID
            avatar_url (string): The URL for an icon that represents your channel
            template_support (boolean): If true, enables templates logic on UI. Requires getTemplates endpoint implemented. Find out more [here](https://pipedrive.readme.io/docs/implementing-messaging-app-extension).
            provider_type (string): It controls the icons (like the icon next to the conversation)

        Returns:
            dict[str, Any]: The channel registered

        Tags:
            Channels
        """
        request_body = {
            'name': name,
            'provider_channel_id': provider_channel_id,
            'avatar_url': avatar_url,
            'template_support': template_support,
            'provider_type': provider_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/channels"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_delete_channel_by_id(self, id) -> dict[str, Any]:
        """
        Deletes a channel specified by the ID in the path and returns an empty response on success.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: The channel was deleted

        Tags:
            Channels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/channels/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_receive_message(self, id, channel_id, sender_id, conversation_id, message, status, created_at, reply_by=None, conversation_link=None, attachments=None) -> dict[str, Any]:
        """
        Receives messages on a specified channel and returns a success or error status.

        Args:
            id (string): The ID of the message
            channel_id (string): The channel ID as in the provider
            sender_id (string): The ID of the provider's user that sent the message
            conversation_id (string): The ID of the conversation
            message (string): The body of the message
            status (string): The status of the message
            created_at (string): The date and time when the message was created in the provider, in UTC. Format: YYYY-MM-DD HH:MM
            reply_by (string): The date and time when the message can no longer receive a reply, in UTC. Format: YYYY-MM-DD HH:MM
            conversation_link (string): A URL that can open the conversation in the provider's side
            attachments (array): The list of attachments available in the message

        Returns:
            dict[str, Any]: The message was registered in the conversation

        Tags:
            Channels
        """
        request_body = {
            'id': id,
            'channel_id': channel_id,
            'sender_id': sender_id,
            'conversation_id': conversation_id,
            'message': message,
            'status': status,
            'created_at': created_at,
            'reply_by': reply_by,
            'conversation_link': conversation_link,
            'attachments': attachments,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/channels/messages/receive"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def channels_delete_conversation(self, channel_id, conversation_id) -> dict[str, Any]:
        """
        Deletes a specific conversation within a channel and returns a success status upon completion.

        Args:
            channel_id (string): channel-id
            conversation_id (string): conversation-id

        Returns:
            dict[str, Any]: The conversation was deleted

        Tags:
            Channels
        """
        if channel_id is None:
            raise ValueError("Missing required parameter 'channel-id'")
        if conversation_id is None:
            raise ValueError("Missing required parameter 'conversation-id'")
        url = f"{self.base_url}/channels/{channel_id}/conversations/{conversation_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def currencies_get_all_supported(self, term=None) -> dict[str, Any]:
        """
        Retrieves a list of currencies based on a search term using the "GET" method at the "/currencies" path.

        Args:
            term (string): Optional search term that is searched for from currency's name and/or code

        Returns:
            dict[str, Any]: The list of supported currencies

        Tags:
            Currencies
        """
        url = f"{self.base_url}/currencies"
        query_params = {k: v for k, v in [('term', term)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_get_all_deals(self, user_id=None, filter_id=None, stage_id=None, status=None, start=None, limit=None, sort=None, owned_by_you=None) -> dict[str, Any]:
        """
        Retrieves a list of deals based on specified parameters such as user ID, filter ID, stage ID, status, and sorting options, allowing for pagination and filtering by ownership.

        Args:
            user_id (integer): If supplied, only deals matching the given user will be returned. However, `filter_id` and `owned_by_you` takes precedence over `user_id` when supplied.
            filter_id (integer): The ID of the filter to use
            stage_id (integer): If supplied, only deals within the given stage will be returned
            status (string): Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).
            owned_by_you (number): When supplied, only deals owned by you are returned. However, `filter_id` takes precedence over `owned_by_you` when both are supplied.

        Returns:
            dict[str, Any]: Get all deals

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals"
        query_params = {k: v for k, v in [('user_id', user_id), ('filter_id', filter_id), ('stage_id', stage_id), ('status', status), ('start', start), ('limit', limit), ('sort', sort), ('owned_by_you', owned_by_you)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_create_deal(self, title, value=None, label=None, currency=None, user_id=None, person_id=None, org_id=None, pipeline_id=None, stage_id=None, status=None, add_time=None, won_time=None, lost_time=None, close_time=None, expected_close_date=None, probability=None, lost_reason=None, visible_to=None) -> dict[str, Any]:
        """
        Creates a new deal in a CRM system using the POST method at the "/deals" endpoint and returns a success response with a status code of 201.

        Args:
            title (string): The title of the deal
            value (string): The value of the deal. If omitted, value will be set to 0.
            label (array): The array of the labels IDs.
            currency (string): The currency of the deal. Accepts a 3-character currency code. If omitted, currency will be set to the default currency of the authorized user.
            user_id (integer): The ID of the user which will be the owner of the created deal. If not provided, the user making the request will be used.
            person_id (integer): The ID of a person which this deal will be linked to. If the person does not exist yet, it needs to be created first. This property is required unless `org_id` is specified.
            org_id (integer): The ID of an organization which this deal will be linked to. If the organization does not exist yet, it needs to be created first. This property is required unless `person_id` is specified.
            pipeline_id (integer): The ID of the pipeline this deal will be added to. By default, the deal will be added to the first stage of the specified pipeline. Please note that `pipeline_id` and `stage_id` should not be used together as `pipeline_id` will be ignored.
            stage_id (integer): The ID of the stage this deal will be added to. Please note that a pipeline will be assigned automatically based on the `stage_id`. If omitted, the deal will be placed in the first stage of the default pipeline.
            status (string): open = Open, won = Won, lost = Lost, deleted = Deleted. If omitted, status will be set to open.
            add_time (string): The optional creation date & time of the deal in UTC. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS
            won_time (string): The optional date and time of changing the deal status as won in UTC. Format: YYYY-MM-DD HH:MM:SS. Can be set only when deal `status` is already Won. Can not be used together with `lost_time`.
            lost_time (string): The optional date and time of changing the deal status as lost in UTC. Format: YYYY-MM-DD HH:MM:SS. Can be set only when deal `status` is already Lost. Can not be used together with `won_time`.
            close_time (string): The optional date and time of closing the deal in UTC. Format: YYYY-MM-DD HH:MM:SS.
            expected_close_date (string): The expected close date of the deal. In ISO 8601 format: YYYY-MM-DD.
            probability (number): The success probability percentage of the deal. Used/shown only when `deal_probability` for the pipeline of the deal is enabled.
            lost_reason (string): The optional message about why the deal was lost (to be used when status = lost)
            visible_to (string): The visibility of the deal. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>

        Returns:
            dict[str, Any]: Add a deal

        Tags:
            Deals
        """
        request_body = {
            'title': title,
            'value': value,
            'label': label,
            'currency': currency,
            'user_id': user_id,
            'person_id': person_id,
            'org_id': org_id,
            'pipeline_id': pipeline_id,
            'stage_id': stage_id,
            'status': status,
            'add_time': add_time,
            'won_time': won_time,
            'lost_time': lost_time,
            'close_time': close_time,
            'expected_close_date': expected_close_date,
            'probability': probability,
            'lost_reason': lost_reason,
            'visible_to': visible_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_delete_bulk(self, ids) -> dict[str, Any]:
        """
        Deletes multiple deals by their comma-separated IDs and returns a success status.

        Args:
            ids (string): The comma-separated IDs that will be deleted

        Returns:
            dict[str, Any]: Delete multiple deals in bulk

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def dealsget_all_deals(self, cursor=None, limit=None, since=None, until=None, user_id=None, stage_id=None, status=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of deals with filtering options for cursor-based navigation, date ranges, user association, stage, and status.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed. Example: '100'.
            since (string): The time boundary that points to the start of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            until (string): The time boundary that points to the end of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            user_id (integer): If supplied, only deals matching the given user will be returned
            stage_id (integer): If supplied, only deals within the given stage will be returned
            status (string): Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.

        Returns:
            dict[str, Any]: Get all deals

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals/collection"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('since', since), ('until', until), ('user_id', user_id), ('stage_id', stage_id), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_search_by_title_and_notes(self, term, fields=None, exact_match=None, person_id=None, organization_id=None, status=None, include_fields=None, start=None, limit=None) -> Any:
        """
        Retrieves a list of deals based on search criteria, including terms, fields, and filters such as person ID, organization ID, status, and other parameters, using the GET method at the "/deals/search" endpoint.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all of them. Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            person_id (integer): Will filter deals by the provided person ID. The upper limit of found deals associated with the person is 2000.
            organization_id (integer): Will filter deals by the provided organization ID. The upper limit of found deals associated with the organization is 2000.
            status (string): Will filter deals by the provided specific status. open = Open, won = Won, lost = Lost. The upper limit of found deals associated with the status is 2000.
            include_fields (string): Supports including optional fields in the results which are not provided by default
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals/search"
        query_params = {k: v for k, v in [('term', term), ('fields', fields), ('exact_match', exact_match), ('person_id', person_id), ('organization_id', organization_id), ('status', status), ('include_fields', include_fields), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_get_summary(self, status=None, filter_id=None, user_id=None, stage_id=None) -> dict[str, Any]:
        """
        Retrieves a summary of deals based on specified parameters such as status, filter ID, user ID, and stage ID using the GET method at the "/deals/summary" path.

        Args:
            status (string): Only fetch deals with a specific status. open = Open, won = Won, lost = Lost.
            filter_id (integer): <code>user_id</code> will not be considered. Only deals matching the given filter will be returned.
            user_id (integer): Only deals matching the given user will be returned. `user_id` will not be considered if you use `filter_id`.
            stage_id (integer): Only deals within the given stage will be returned

        Returns:
            dict[str, Any]: Get the summary of the deals

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals/summary"
        query_params = {k: v for k, v in [('status', status), ('filter_id', filter_id), ('user_id', user_id), ('stage_id', stage_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_get_timeline_data(self, start_date, interval, amount, field_key, user_id=None, pipeline_id=None, filter_id=None, exclude_deals=None, totals_convert_currency=None) -> dict[str, Any]:
        """
        Retrieves a timeline of deal events, allowing users to list and group deals by specified intervals and criteria, including start date, interval type, and additional filters like user or pipeline, and optionally convert totals into a specified currency.

        Args:
            start_date (string): The date when the first interval starts. Format: YYYY-MM-DD.
            interval (string): The type of the interval<table><tr><th>Value</th><th>Description</th></tr><tr><td>`day`</td><td>Day</td></tr><tr><td>`week`</td><td>A full week (7 days) starting from `start_date`</td></tr><tr><td>`month`</td><td>A full month (depending on the number of days in given month) starting from `start_date`</td></tr><tr><td>`quarter`</td><td>A full quarter (3 months) starting from `start_date`</td></tr></table>
            amount (integer): The number of given intervals, starting from `start_date`, to fetch. E.g. 3 (months).
            field_key (string): The date field key which deals will be retrieved from
            user_id (integer): If supplied, only deals matching the given user will be returned
            pipeline_id (integer): If supplied, only deals matching the given pipeline will be returned
            filter_id (integer): If supplied, only deals matching the given filter will be returned
            exclude_deals (number): Whether to exclude deals list (1) or not (0). Note that when deals are excluded, the timeline summary (counts and values) is still returned.
            totals_convert_currency (string): The 3-letter currency code of any of the supported currencies. When supplied, `totals_converted` is returned per each interval which contains the currency-converted total amounts in the given currency. You may also set this parameter to `default_currency` in which case the user's default currency is used.

        Returns:
            dict[str, Any]: Get open and won deals, grouped by the defined interval of time

        Tags:
            Deals
        """
        url = f"{self.base_url}/deals/timeline"
        query_params = {k: v for k, v in [('start_date', start_date), ('interval', interval), ('amount', amount), ('field_key', field_key), ('user_id', user_id), ('pipeline_id', pipeline_id), ('filter_id', filter_id), ('exclude_deals', exclude_deals), ('totals_convert_currency', totals_convert_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes a deal by its ID using the "DELETE" method, removing the specified deal from the system.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves details about a specific deal by its ID using the API endpoint "/deals/{id}" with the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a deal by its ID

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_update_properties(self, id, title=None, value=None, label=None, currency=None, user_id=None, person_id=None, org_id=None, pipeline_id=None, stage_id=None, status=None, won_time=None, lost_time=None, close_time=None, expected_close_date=None, probability=None, lost_reason=None, visible_to=None) -> dict[str, Any]:
        """
        Updates a specific deal by replacing it with new data at the path "/deals/{id}".

        Args:
            id (string): id
            title (string): The title of the deal
            value (string): The value of the deal.
            label (array): Array of the deal labels IDs.
            currency (string): The currency of the deal. Accepts a 3-character currency code.
            user_id (integer): The ID of the user which will be the new owner of the deal.
            person_id (integer): The ID of a person which this deal will be linked to. If the person does not exist yet, it needs to be created first.
            org_id (integer): The ID of an organization which this deal will be linked to. If the organization does not exist yet, it needs to be created first.
            pipeline_id (integer): The ID of the pipeline this deal will be added to. By default, the deal will be added to the first stage of the specified pipeline. Please note that `pipeline_id` and `stage_id` should not be used together as `pipeline_id` will be ignored.
            stage_id (integer): The ID of the stage this deal will be added to. Please note that a pipeline will be assigned automatically based on the `stage_id`.
            status (string): open = Open, won = Won, lost = Lost, deleted = Deleted.
            won_time (string): The optional date and time of changing the deal status as won in UTC. Format: YYYY-MM-DD HH:MM:SS. Can be set only when deal `status` is already Won. Can not be used together with `lost_time`.
            lost_time (string): The optional date and time of changing the deal status as lost in UTC. Format: YYYY-MM-DD HH:MM:SS. Can be set only when deal `status` is already Lost. Can not be used together with `won_time`.
            close_time (string): The optional date and time of closing the deal in UTC. Format: YYYY-MM-DD HH:MM:SS.
            expected_close_date (string): The expected close date of the deal. In ISO 8601 format: YYYY-MM-DD.
            probability (number): The success probability percentage of the deal. Used/shown only when `deal_probability` for the pipeline of the deal is enabled.
            lost_reason (string): The optional message about why the deal was lost (to be used when status = lost)
            visible_to (string): The visibility of the deal. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>

        Returns:
            dict[str, Any]: Add a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'title': title,
            'value': value,
            'label': label,
            'currency': currency,
            'user_id': user_id,
            'person_id': person_id,
            'org_id': org_id,
            'pipeline_id': pipeline_id,
            'stage_id': stage_id,
            'status': status,
            'won_time': won_time,
            'lost_time': lost_time,
            'close_time': close_time,
            'expected_close_date': expected_close_date,
            'probability': probability,
            'lost_reason': lost_reason,
            'visible_to': visible_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_activities(self, id, start=None, limit=None, done=None, exclude=None) -> Any:
        """
        Retrieves a list of activities associated with a specific deal, optionally filtered by status and pagination parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            done (number): Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted, returns both Done and Not done activities.
            exclude (string): A comma-separated string of activity IDs to exclude from result

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/activities"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('done', done), ('exclude', exclude)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_duplicate_deal(self, id) -> dict[str, Any]:
        """
        Creates a duplicate of the specified deal using its ID and returns the new deal in the response.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Duplicate a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/duplicate"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_deal_files(self, id, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of files associated with a specific deal by ID, allowing pagination and sorting of the results.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `product_id`, `add_time`, `update_time`, `file_name`, `file_type`, `file_size`, `comment`.

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/files"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_deal_updates(self, id, start=None, limit=None, all_changes=None, items=None) -> Any:
        """
        Retrieves the workflow history and associated changes for a specific deal, optionally filtered by parameters like start time, limit, and item types.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            all_changes (string): Whether to show custom field updates or not. 1 = Include custom field changes. If omitted returns changes without custom field updates.
            items (string): A comma-separated string for filtering out item specific updates. (Possible values - call, activity, plannedActivity, change, note, deal, file, dealChange, personChange, organizationChange, follower, dealFollower, personFollower, organizationFollower, participant, comment, mailMessage, mailMessageWithAttachment, invoice, document, marketing_campaign_stat, marketing_status_change).

        Returns:
            Any: Get the deal updates

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/flow"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('all_changes', all_changes), ('items', items)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_participants_changelog(self, id, limit=None, cursor=None) -> dict[str, Any]:
        """
        Retrieves paginated changelog data tracking participant-related modifications for a specific deal using cursor-based pagination.

        Args:
            id (string): id
            limit (integer): Items shown per page
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page

        Returns:
            dict[str, Any]: Get participant changelogs for a given deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/participantsChangelog"
        query_params = {k: v for k, v in [('limit', limit), ('cursor', cursor)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_followers(self, id) -> Any:
        """
        Retrieves a list of users following a deal, identified by its ID, using the GET method at the "/deals/{id}/followers" path.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/followers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_add_follower(self, id, user_id) -> dict[str, Any]:
        """
        Adds followers to a specified deal and returns a success status.

        Args:
            id (string): id
            user_id (integer): The ID of the user

        Returns:
            dict[str, Any]: Add a follower to a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'user_id': user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}/followers"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_remove_follower(self, id, follower_id) -> dict[str, Any]:
        """
        Removes a specific follower from a deal using the "DELETE" method at the "/deals/{id}/followers/{follower_id}" endpoint.

        Args:
            id (string): id
            follower_id (string): follower_id

        Returns:
            dict[str, Any]: Delete a follower from a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if follower_id is None:
            raise ValueError("Missing required parameter 'follower_id'")
        url = f"{self.base_url}/deals/{id}/followers/{follower_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_mail_messages(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of mail messages associated with a specific deal identified by its ID, allowing pagination through optional start and limit parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/mailMessages"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_merge_deals(self, id, merge_with_id) -> dict[str, Any]:
        """
        Merges a specific deal identified by its ID with another deal and returns the merged result.

        Args:
            id (string): id
            merge_with_id (integer): The ID of the deal that the deal will be merged with

        Returns:
            dict[str, Any]: Merges a deal with another deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'merge_with_id': merge_with_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}/merge"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_participants(self, id, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves participants associated with a specific deal, including their marketing status if applicable, and supports pagination parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: Get all deal participants by the DealID

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/participants"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_add_participant(self, id, person_id) -> dict[str, Any]:
        """
        Lists participants associated with a specific deal in Pipedrive using the provided deal ID.

        Args:
            id (string): id
            person_id (integer): The ID of the person

        Returns:
            dict[str, Any]: Add new participant to the deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'person_id': person_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}/participants"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_delete_participant(self, id, deal_participant_id) -> dict[str, Any]:
        """
        Removes a participant from a deal using the DELETE method at the endpoint "/deals/{id}/participants/{deal_participant_id}".

        Args:
            id (string): id
            deal_participant_id (string): deal_participant_id

        Returns:
            dict[str, Any]: Delete a participant from a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if deal_participant_id is None:
            raise ValueError("Missing required parameter 'deal_participant_id'")
        url = f"{self.base_url}/deals/{id}/participants/{deal_participant_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_permitted_users(self, id) -> Any:
        """
        Retrieves the list of users with permission to access a specific deal in Pipedrive.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/permittedUsers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_persons_associated(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of persons associated with a specific deal, optionally paginated using start and limit query parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/persons"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_list_deal_products(self, id, start=None, limit=None, include_product_data=None) -> Any:
        """
        Retrieves a list of products associated with a specific deal, optionally including product data and pagination support.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            include_product_data (number): Whether to fetch product data along with each attached product (1) or not (0, default)

        Returns:
            Any: Success

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/deals/{id}/products"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('include_product_data', include_product_data)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_add_product_to_deal(self, id, product_id, item_price, quantity, discount=0, discount_type="percentage", duration=1, duration_unit=None, product_variation_id=None, comments=None, tax=0, tax_method=None, enabled_flag=True) -> dict[str, Any]:
        """
        Adds one or more products to a deal identified by the specified ID and returns a success status.

        Args:
            id (string): id
            product_id (integer): The ID of the product to use
            item_price (number): The price at which this product will be added to the deal
            quantity (integer): Quantity – e.g. how many items of this product will be added to the deal
            discount (number): The value of the discount. The `discount_type` field can be used to specify whether the value is an amount or a percentage.
            discount_type (string): The type of the discount's value.
            duration (number): The duration of the product. If omitted, will be set to 1.
            duration_unit (string): The unit duration of the product
            product_variation_id (integer): The ID of the product variation to use. When omitted, no variation will be used.
            comments (string): A textual comment associated with this product-deal attachment
            tax (number): The tax percentage
            tax_method (string): The tax option to be applied to the products. When using `inclusive`, the tax percentage will already be included in the price. When using `exclusive`, the tax will not be included in the price. When using `none`, no tax will be added. Use the `tax` field for defining the tax percentage amount. By default, the user setting value for tax options will be used. Changing this in one product affects the rest of the products attached to the deal.
            enabled_flag (boolean): Whether the product is enabled for a deal or not. This makes it possible to add products to a deal with a specific price and discount criteria, but keep them disabled, which refrains them from being included in the deal value calculation. When omitted, the product will be marked as enabled by default.

        Returns:
            dict[str, Any]: Add a product to the deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'product_id': product_id,
            'item_price': item_price,
            'quantity': quantity,
            'discount': discount,
            'discount_type': discount_type,
            'duration': duration,
            'duration_unit': duration_unit,
            'product_variation_id': product_variation_id,
            'comments': comments,
            'tax': tax,
            'tax_method': tax_method,
            'enabled_flag': enabled_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}/products"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_update_product_attachment(self, id, product_attachment_id, product_id=None, item_price=None, quantity=None, discount=0, discount_type="percentage", duration=1, duration_unit=None, product_variation_id=None, comments=None, tax=0, tax_method=None, enabled_flag=True) -> dict[str, Any]:
        """
        Updates or replaces product attachment information associated with a specific deal using the provided `id` and `product_attachment_id`.

        Args:
            id (string): id
            product_attachment_id (string): product_attachment_id
            product_id (integer): The ID of the product to use
            item_price (number): The price at which this product will be added to the deal
            quantity (integer): How many items of this product will be added to the deal
            discount (number): The value of the discount. The `discount_type` field can be used to specify whether the value is an amount or a percentage.
            discount_type (string): The type of the discount's value.
            duration (number): The duration of the product
            duration_unit (string): The unit duration of the product
            product_variation_id (integer): The ID of the product variation to use. When omitted, no variation will be used.
            comments (string): A textual comment associated with this product-deal attachment
            tax (number): The tax percentage
            tax_method (string): The tax option to be applied to the products. When using `inclusive`, the tax percentage will already be included in the price. When using `exclusive`, the tax will not be included in the price. When using `none`, no tax will be added. Use the `tax` field for defining the tax percentage amount.
            enabled_flag (boolean): Whether the product is enabled for a deal or not. This makes it possible to add products to a deal with a specific price and discount criteria, but keep them disabled, which refrains them from being included in the deal value calculation. When omitted, the product will be marked as enabled by default.

        Returns:
            dict[str, Any]: Update product attachment details

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if product_attachment_id is None:
            raise ValueError("Missing required parameter 'product_attachment_id'")
        request_body = {
            'product_id': product_id,
            'item_price': item_price,
            'quantity': quantity,
            'discount': discount,
            'discount_type': discount_type,
            'duration': duration,
            'duration_unit': duration_unit,
            'product_variation_id': product_variation_id,
            'comments': comments,
            'tax': tax,
            'tax_method': tax_method,
            'enabled_flag': enabled_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/deals/{id}/products/{product_attachment_id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deals_delete_attached_product(self, id, product_attachment_id) -> dict[str, Any]:
        """
        Deletes a specific product attachment associated with a deal identified by both IDs and returns a success status upon removal.

        Args:
            id (string): id
            product_attachment_id (string): product_attachment_id

        Returns:
            dict[str, Any]: Delete an attached product from a deal

        Tags:
            Deals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if product_attachment_id is None:
            raise ValueError("Missing required parameter 'product_attachment_id'")
        url = f"{self.base_url}/deals/{id}/products/{product_attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_get_all_fields(self, start=None, limit=None) -> Any:
        """
        Retrieves all deal fields configuration with pagination support using start and limit parameters.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        url = f"{self.base_url}/dealFields"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_add_new_field(self, name, field_type, options=None, add_visible_flag=True) -> Any:
        """
        Creates a new custom deal field in the Pipedrive CRM system.

        Args:
            name (string): The name of the field
            field_type (string): The type of the field<table><tr><th>Value</th><th>Description</th></tr><tr><td>`address`</td><td>Address field (has multiple subfields, autocompleted by Google Maps)</td></tr><tr><td>`date`</td><td>Date (format YYYY-MM-DD)</td></tr><tr><td>`daterange`</td><td>Date-range field (has a start date and end date value, both YYYY-MM-DD)</td></tr><tr><td>`double`</td><td>Numeric value</td></tr><tr><td>`enum`</td><td>Options field with a single possible chosen option</td></tr><tr></tr><tr><td>`monetary`</td><td>Monetary field (has a numeric value and a currency value)</td></tr><tr><td>`org`</td><td>Organization field (contains an organization ID which is stored on the same account)</td></tr><tr><td>`people`</td><td>Person field (contains a person ID which is stored on the same account)</td></tr><tr><td>`phone`</td><td>Phone field (up to 255 numbers and/or characters)</td></tr><tr><td>`set`</td><td>Options field with a possibility of having multiple chosen options</td></tr><tr><td>`text`</td><td>Long text (up to 65k characters)</td></tr><tr><td>`time`</td><td>Time field (format HH:MM:SS)</td></tr><tr><td>`timerange`</td><td>Time-range field (has a start time and end time value, both HH:MM:SS)</td></tr><tr><td>`user`</td><td>User field (contains a user ID of another Pipedrive user)</td></tr><tr><td>`varchar`</td><td>Text (up to 255 characters)</td></tr><tr><td>`varchar_auto`</td><td>Autocomplete text (up to 255 characters)</td></tr><tr><td>`visible_to`</td><td>System field that keeps item's visibility setting</td></tr></table>
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. Example: `[{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in the 'add new' modal or not (both in the web and mobile app)

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
            'field_type': field_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/dealFields"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_delete_multiple_bulk(self, ids) -> Any:
        """
        Deletes multiple custom deal fields in Pipedrive by specifying their IDs via a DELETE request to the "/dealFields" endpoint.

        Args:
            ids (string): The comma-separated field IDs to delete

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        url = f"{self.base_url}/dealFields"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_get_one_field(self, id) -> Any:
        """
        Retrieves the details of a specific deal field by its ID, including schema and configuration.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/dealFields/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_mark_as_deleted(self, id) -> Any:
        """
        Deletes a specific deal field by its ID using the Pipedrive API.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/dealFields/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deal_fields_update_field(self, id, name=None, options=None, add_visible_flag=True) -> Any:
        """
        Updates an existing deal field's configuration by ID, modifying its properties and schema definition.

        Args:
            id (string): id
            name (string): The name of the field
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. All active items must be supplied and already existing items must have their ID supplied. New items only require a label. Example: `[{"id":123,"label":"Existing Item"},{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in 'add new' modal or not (both in web and mobile app)

        Returns:
            Any: Success

        Tags:
            DealFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/dealFields/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def files_get_all_files(self, start=None, limit=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of files using the "GET" method, allowing optional filtering by start position, number of items, and sorting order.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `product_id`, `add_time`, `update_time`, `file_name`, `file_type`, `file_size`, `comment`.

        Returns:
            dict[str, Any]: Get data about all files uploaded to Pipedrive

        Tags:
            Files
        """
        url = f"{self.base_url}/files"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()



    def files_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes a specified file using the provided ID and returns a success status upon completion.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete a file from Pipedrive

        Tags:
            Files
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/files/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def files_get_one_file(self, id) -> dict[str, Any]:
        """
        Retrieves a file resource identified by the provided ID using the GET method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get data about one specific file uploaded to Pipedrive

        Tags:
            Files
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/files/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()


    def files_download_file(self, id) -> Any:
        """
        Downloads a file from the server using the provided ID and returns the file content upon success.

        Args:
            id (string): id

        Returns:
            Any: success

        Tags:
            Files
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/files/{id}/download"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_delete_bulk(self, ids) -> Any:
        """
        Deletes one or more filters identified by their IDs passed as query parameters.

        Args:
            ids (string): The comma-separated filter IDs to delete

        Returns:
            Any: Success

        Tags:
            Filters
        """
        url = f"{self.base_url}/filters"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_get_all(self, type=None) -> Any:
        """
        Retrieves a list of filters based on the specified type.

        Args:
            type (string): The types of filters to fetch

        Returns:
            Any: Success

        Tags:
            Filters
        """
        url = f"{self.base_url}/filters"
        query_params = {k: v for k, v in [('type', type)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_add_new_filter(self, name, conditions, type) -> Any:
        """
        Applies filters using the API at the "/filters" endpoint via the POST method and returns a response.

        Args:
            name (string): The name of the filter
            conditions (object): The conditions of the filter as a JSON object. Please note that a maximum of 16 conditions is allowed per filter and `date` values must be supplied in the `YYYY-MM-DD` format. It requires a minimum structure as follows: `{"glue":"and","conditions":[{"glue":"and","conditions": [CONDITION_OBJECTS]},{"glue":"or","conditions":[CONDITION_OBJECTS]}]}`. Replace `CONDITION_OBJECTS` with JSON objects of the following structure: `{"object":"","field_id":"", "operator":"","value":"", "extra_value":""}` or leave the array empty. Depending on the object type you should use another API endpoint to get `field_id`. There are five types of objects you can choose from: `"person"`, `"deal"`, `"organization"`, `"product"`, `"activity"` and you can use these types of operators depending on what type of a field you have: `"IS NOT NULL"`, `"IS NULL"`, `"<="`, `">="`, `"<"`, `">"`, `"!="`, `"="`, `"LIKE '$%'"`, `"LIKE '%$%'"`, `"NOT LIKE '$%'"`. To get a better understanding of how filters work try creating them directly from the Pipedrive application.
            type (string): The type of filter to create

        Returns:
            Any: Success

        Tags:
            Filters
        """
        request_body = {
            'name': name,
            'conditions': conditions,
            'type': type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/filters"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_get_helpers(self) -> dict[str, Any]:
        """
        Retrieves a list of filter helper resources.

        Returns:
            dict[str, Any]: Success

        Tags:
            Filters
        """
        url = f"{self.base_url}/filters/helpers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_mark_as_deleted(self, id) -> Any:
        """
        Deletes the specified filter by its ID and returns a success response upon completion.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Filters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/filters/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_get_details(self, id) -> Any:
        """
        Retrieves a specific filter by its unique identifier from the API.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Filters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/filters/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def filters_update_filter(self, id, conditions, name=None) -> Any:
        """
        Updates a filter with a specified ID using the PUT method, allowing for modification of its properties.

        Args:
            id (string): id
            conditions (object): The conditions of the filter as a JSON object. Please note that a maximum of 16 conditions is allowed per filter and `date` values must be supplied in the `YYYY-MM-DD` format. It requires a minimum structure as follows: `{"glue":"and","conditions":[{"glue":"and","conditions": [CONDITION_OBJECTS]},{"glue":"or","conditions":[CONDITION_OBJECTS]}]}`. Replace `CONDITION_OBJECTS` with JSON objects of the following structure: `{"object":"","field_id":"", "operator":"","value":"", "extra_value":""}` or leave the array empty. Depending on the object type you should use another API endpoint to get `field_id`. There are five types of objects you can choose from: `"person"`, `"deal"`, `"organization"`, `"product"`, `"activity"` and you can use these types of operators depending on what type of a field you have: `"IS NOT NULL"`, `"IS NULL"`, `"<="`, `">="`, `"<"`, `">"`, `"!="`, `"="`, `"LIKE '$%'"`, `"LIKE '%$%'"`, `"NOT LIKE '$%'"`. To get a better understanding of how filters work try creating them directly from the Pipedrive application.
            name (string): The name of the filter

        Returns:
            Any: Success

        Tags:
            Filters
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'conditions': conditions,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/filters/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def goals_create_report(self, assignee, type, expected_outcome, duration, interval, title=None) -> dict[str, Any]:
        """
        Creates a new goal entry in the system and returns a status message upon successful creation.

        Args:
            assignee (object): Who this goal is assigned to. It requires the following JSON structure: `{ "id": "1", "type": "person" }`. `type` can be either `person`, `company` or `team`. ID of the assignee person, company or team.
            type (object): The type of the goal. It requires the following JSON structure: `{ "name": "deals_started", "params": { "pipeline_id": [1, 2], "activity_type_id": [9] } }`. Type can be one of: `deals_won`, `deals_progressed`, `activities_completed`, `activities_added`, `deals_started` or `revenue_forecast`. `params` can include `pipeline_id`, `stage_id` or `activity_type_id`. `stage_id` is related to only `deals_progressed` type of goals and `activity_type_id` to `activities_completed` or `activities_added` types of goals. The `pipeline_id` and `activity_type_id` need to be given as an array of integers. To track the goal in all pipelines, set `pipeline_id` as `null` and similarly, to track the goal for all activities, set `activity_type_id` as `null`.”
            expected_outcome (object): The expected outcome of the goal. Expected outcome can be tracked either by `quantity` or by `sum`. It requires the following JSON structure: `{ "target": "50", "tracking_metric": "quantity" }` or `{ "target": "50", "tracking_metric": "sum", "currency_id": 1 }`. `currency_id` should only be added to `sum` type of goals.
            duration (object): The date when the goal starts and ends. It requires the following JSON structure: `{ "start": "2019-01-01", "end": "2022-12-31" }`. Date in format of YYYY-MM-DD. "end" can be set to `null` for an infinite, open-ended goal.
            interval (string): The interval of the goal
            title (string): The title of the goal

        Returns:
            dict[str, Any]: Successful response containing payload in the `data.goal` object

        Tags:
            Goals
        """
        request_body = {
            'title': title,
            'assignee': assignee,
            'type': type,
            'expected_outcome': expected_outcome,
            'duration': duration,
            'interval': interval,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def goals_get_by_criteria(self, type_name=None, title=None, is_active=None, assignee_id=None, assignee_type=None, expected_outcome_target=None, expected_outcome_tracking_metric=None, expected_outcome_currency_id=None, type_params_pipeline_id=None, type_params_stage_id=None, type_params_activity_type_id=None, period_start=None, period_end=None) -> dict[str, Any]:
        """
        Retrieves a list of goals based on specified criteria, such as type, title, status, assignee, expected outcome details, and timeframe, using the "GET" method at the "/goals/find" endpoint.

        Args:
            type_name (string): The type of the goal. If provided, everyone's goals will be returned.
            title (string): The title of the goal
            is_active (boolean): Whether the goal is active or not
            assignee_id (integer): The ID of the user who's goal to fetch. When omitted, only your goals will be returned.
            assignee_type (string): The type of the goal's assignee. If provided, everyone's goals will be returned.
            expected_outcome_target (number): The numeric value of the outcome. If provided, everyone's goals will be returned.
            expected_outcome_tracking_metric (string): The tracking metric of the expected outcome of the goal. If provided, everyone's goals will be returned.
            expected_outcome_currency_id (integer): The numeric ID of the goal's currency. Only applicable to goals with `expected_outcome.tracking_metric` with value `sum`. If provided, everyone's goals will be returned.
            type_params_pipeline_id (array): An array of pipeline IDs or `null` for all pipelines. If provided, everyone's goals will be returned.
            type_params_stage_id (integer): The ID of the stage. Applicable to only `deals_progressed` type of goals. If provided, everyone's goals will be returned.
            type_params_activity_type_id (array): An array of IDs or `null` for all activity types. Only applicable for `activities_completed` and/or `activities_added` types of goals. If provided, everyone's goals will be returned.
            period_start (string): The start date of the period for which to find goals. Date in format of YYYY-MM-DD. When `period.start` is provided, `period.end` must be provided too.
            period_end (string): The end date of the period for which to find goals. Date in format of YYYY-MM-DD.

        Returns:
            dict[str, Any]: Successful response containing payload in the `data.goal` object

        Tags:
            Goals
        """
        url = f"{self.base_url}/goals/find"
        query_params = {k: v for k, v in [('type.name', type_name), ('title', title), ('is_active', is_active), ('assignee.id', assignee_id), ('assignee.type', assignee_type), ('expected_outcome.target', expected_outcome_target), ('expected_outcome.tracking_metric', expected_outcome_tracking_metric), ('expected_outcome.currency_id', expected_outcome_currency_id), ('type.params.pipeline_id', type_params_pipeline_id), ('type.params.stage_id', type_params_stage_id), ('type.params.activity_type_id', type_params_activity_type_id), ('period.start', period_start), ('period.end', period_end)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def goals_update_existing_goal(self, id, title=None, assignee=None, type=None, expected_outcome=None, duration=None, interval=None) -> dict[str, Any]:
        """
        Updates an existing goal with the specified ID using the provided data and returns a success response upon completion.

        Args:
            id (string): id
            title (string): The title of the goal
            assignee (object): Who this goal is assigned to. It requires the following JSON structure: `{ "id": "1", "type": "person" }`. `type` can be either `person`, `company` or `team`. ID of the assignee person, company or team.
            type (object): The type of the goal. It requires the following JSON structure: `{ "name": "deals_started", "params": { "pipeline_id": [1, 2], "activity_type_id": [9] } }`. Type can be one of: `deals_won`, `deals_progressed`, `activities_completed`, `activities_added`, `deals_started` or `revenue_forecast`. `params` can include `pipeline_id`, `stage_id` or `activity_type_id`. `stage_id` is related to only `deals_progressed` type of goals and `activity_type_id` to `activities_completed` or `activities_added` types of goals. The `pipeline_id` and `activity_type_id` need to be given as an array of integers. To track the goal in all pipelines, set `pipeline_id` as `null` and similarly, to track the goal for all activities, set `activity_type_id` as `null`.”
            expected_outcome (object): The expected outcome of the goal. Expected outcome can be tracked either by `quantity` or by `sum`. It requires the following JSON structure: `{ "target": "50", "tracking_metric": "quantity" }` or `{ "target": "50", "tracking_metric": "sum", "currency_id": 1 }`. `currency_id` should only be added to `sum` type of goals.
            duration (object): The date when the goal starts and ends. It requires the following JSON structure: `{ "start": "2019-01-01", "end": "2022-12-31" }`. Date in format of YYYY-MM-DD. "end" can be set to `null` for an infinite, open-ended goal.
            interval (string): The interval of the goal

        Returns:
            dict[str, Any]: Successful response containing payload in the `data.goal` object

        Tags:
            Goals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'title': title,
            'assignee': assignee,
            'type': type,
            'expected_outcome': expected_outcome,
            'duration': duration,
            'interval': interval,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def goals_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes a goal identified by its ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response with id 'success' field only

        Tags:
            Goals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/goals/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def goals_get_result(self, id, period_start, period_end) -> dict[str, Any]:
        """
        Retrieves results for a specific goal using a goal ID, optionally filtered by start and end date periods.

        Args:
            id (string): id
            period_start (string): The start date of the period for which to find the goal's progress. Format: YYYY-MM-DD. This date must be the same or after the goal duration start date.
            period_end (string): The end date of the period for which to find the goal's progress. Format: YYYY-MM-DD. This date must be the same or before the goal duration end date.

        Returns:
            dict[str, Any]: Successful response containing payload in the `data.goal` object

        Tags:
            Goals
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/goals/{id}/results"
        query_params = {k: v for k, v in [('period.start', period_start), ('period.end', period_end)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def item_search_search_multiple_items(self, term, item_types=None, fields=None, search_for_related_items=None, exact_match=None, include_fields=None, start=None, limit=None) -> Any:
        """
        Searches for items using optional filters like term, item types, and exact match, supporting pagination and field selection in the results.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            item_types (string): A comma-separated string array. The type of items to perform the search from. Defaults to all.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all. Relevant for each item type are:<br> <table> <tr><th><b>Item type</b></th><th><b>Field</b></th></tr> <tr><td>Deal</td><td>`custom_fields`, `notes`, `title`</td></tr> <tr><td>Person</td><td>`custom_fields`, `email`, `name`, `notes`, `phone`</td></tr> <tr><td>Organization</td><td>`address`, `custom_fields`, `name`, `notes`</td></tr> <tr><td>Product</td><td>`code`, `custom_fields`, `name`</td></tr> <tr><td>Lead</td><td>`custom_fields`, `notes`, `email`, `organization_name`, `person_name`, `phone`, `title`</td></tr> <tr><td>File</td><td>`name`</td></tr> <tr><td>Mail attachment</td><td>`name`</td></tr> <tr><td>Project</td><td> `custom_fields`, `notes`, `title`, `description` </td></tr> </table> <br> Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.<br/> When searching for leads, the email, organization_name, person_name, and phone fields will return results only for leads not linked to contacts. For searching leads by person or organization values, please use `search_for_related_items`.
            search_for_related_items (boolean): When enabled, the response will include up to 100 newest related leads and 100 newest related deals for each found person and organization and up to 100 newest related persons for each found organization
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            include_fields (string): A comma-separated string array. Supports including optional fields in the results which are not provided by default.
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            ItemSearch
        """
        url = f"{self.base_url}/itemSearch"
        query_params = {k: v for k, v in [('term', term), ('item_types', item_types), ('fields', fields), ('search_for_related_items', search_for_related_items), ('exact_match', exact_match), ('include_fields', include_fields), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def item_search_by_field_values(self, term, field_type, field_key, exact_match=None, return_item_ids=None, start=None, limit=None) -> Any:
        """
        Performs a search for specific field values across various entity types, allowing for exact or partial matches, and returns either distinct field values for autocomplete or item IDs based on the specified search criteria.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            field_type (string): The type of the field to perform the search from
            field_key (string): The key of the field to search from. The field key can be obtained by fetching the list of the fields using any of the fields' API GET methods (dealFields, personFields, etc.). Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. The search <b>is</b> case sensitive.
            return_item_ids (boolean): Whether to return the IDs of the matching items or not. When not set or set to `0` or `false`, only distinct values of the searched field are returned. When set to `1` or `true`, the ID of each found item is returned.
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            ItemSearch
        """
        url = f"{self.base_url}/itemSearch/field"
        query_params = {k: v for k, v in [('term', term), ('field_type', field_type), ('exact_match', exact_match), ('field_key', field_key), ('return_item_ids', return_item_ids), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_get_all(self, limit=None, start=None, archived_status=None, owner_id=None, person_id=None, organization_id=None, filter_id=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of leads using the "GET" method at the "/leads" endpoint, allowing filtering by various criteria such as limit, start, archived status, owner ID, person ID, organization ID, filter ID, and sort options.

        Args:
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Example: '100'.
            start (integer): For pagination, the position that represents the first result for the page Example: '0'.
            archived_status (string): Filtering based on the archived status of a lead. If not provided, `All` is used.
            owner_id (integer): If supplied, only leads matching the given user will be returned. However, `filter_id` takes precedence over `owner_id` when supplied. Example: '1'.
            person_id (integer): If supplied, only leads matching the given person will be returned. However, `filter_id` takes precedence over `person_id` when supplied. Example: '1'.
            organization_id (integer): If supplied, only leads matching the given organization will be returned. However, `filter_id` takes precedence over `organization_id` when supplied. Example: '1'.
            filter_id (integer): The ID of the filter to use Example: '1'.
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            Leads
        """
        url = f"{self.base_url}/leads"
        query_params = {k: v for k, v in [('limit', limit), ('start', start), ('archived_status', archived_status), ('owner_id', owner_id), ('person_id', person_id), ('organization_id', organization_id), ('filter_id', filter_id), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_create_lead(self, title, owner_id=None, label_ids=None, person_id=None, organization_id=None, value=None, expected_close_date=None, visible_to=None, was_seen=None) -> dict[str, Any]:
        """
        Creates a new lead by sending a POST request to the "/leads" endpoint, returning a success response upon creation.

        Args:
            title (string): The name of the lead
            owner_id (integer): The ID of the user which will be the owner of the created lead. If not provided, the user making the request will be used.
            label_ids (array): The IDs of the lead labels which will be associated with the lead
            person_id (integer): The ID of a person which this lead will be linked to. If the person does not exist yet, it needs to be created first. This property is required unless `organization_id` is specified.
            organization_id (integer): The ID of an organization which this lead will be linked to. If the organization does not exist yet, it needs to be created first. This property is required unless `person_id` is specified.
            value (object): The potential value of the lead
            expected_close_date (string): The date of when the deal which will be created from the lead is expected to be closed. In ISO 8601 format: YYYY-MM-DD.
            visible_to (string): The visibility of the lead. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            was_seen (boolean): A flag indicating whether the lead was seen by someone in the Pipedrive UI

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            Leads
        """
        request_body = {
            'title': title,
            'owner_id': owner_id,
            'label_ids': label_ids,
            'person_id': person_id,
            'organization_id': organization_id,
            'value': value,
            'expected_close_date': expected_close_date,
            'visible_to': visible_to,
            'was_seen': was_seen,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/leads"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves a lead by its unique identifier from the system.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            Leads
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/leads/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_update_lead_properties(self, id, title=None, owner_id=None, label_ids=None, person_id=None, organization_id=None, is_archived=None, value=None, expected_close_date=None, visible_to=None, was_seen=None) -> dict[str, Any]:
        """
        Updates a specific lead by partially modifying its details using the provided ID.

        Args:
            id (string): id
            title (string): The name of the lead
            owner_id (integer): The ID of the user which will be the owner of the created lead. If not provided, the user making the request will be used.
            label_ids (array): The IDs of the lead labels which will be associated with the lead
            person_id (integer): The ID of a person which this lead will be linked to. If the person does not exist yet, it needs to be created first. A lead always has to be linked to a person or organization or both.

            organization_id (integer): The ID of an organization which this lead will be linked to. If the organization does not exist yet, it needs to be created first. A lead always has to be linked to a person or organization or both.
            is_archived (boolean): A flag indicating whether the lead is archived or not
            value (object): The potential value of the lead
            expected_close_date (string): The date of when the deal which will be created from the lead is expected to be closed. In ISO 8601 format: YYYY-MM-DD.
            visible_to (string): The visibility of the lead. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            was_seen (boolean): A flag indicating whether the lead was seen by someone in the Pipedrive UI

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            Leads
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'title': title,
            'owner_id': owner_id,
            'label_ids': label_ids,
            'person_id': person_id,
            'organization_id': organization_id,
            'is_archived': is_archived,
            'value': value,
            'expected_close_date': expected_close_date,
            'visible_to': visible_to,
            'was_seen': was_seen,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/leads/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_delete_lead(self, id) -> dict[str, Any]:
        """
        Deletes a lead with the specified ID and removes all associated data from the system.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response with id value only. Used in DELETE calls.

        Tags:
            Leads
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/leads/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_list_permitted_users(self, id) -> Any:
        """
        Retrieves a list of permitted users for a specific lead, identified by the provided lead ID, using the GET method on the "/leads/{id}/permittedUsers" endpoint.

        Args:
            id (string): id

        Returns:
            Any: Lists users permitted to access a lead

        Tags:
            Leads
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/leads/{id}/permittedUsers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def leads_search_leads(self, term, fields=None, exact_match=None, person_id=None, organization_id=None, include_fields=None, start=None, limit=None) -> Any:
        """
        Retrieves a list of leads based on search criteria, allowing filtering by term, person, or organization, and supports pagination and field selection.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all of them.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            person_id (integer): Will filter leads by the provided person ID. The upper limit of found leads associated with the person is 2000.
            organization_id (integer): Will filter leads by the provided organization ID. The upper limit of found leads associated with the organization is 2000.
            include_fields (string): Supports including optional fields in the results which are not provided by default
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Leads
        """
        url = f"{self.base_url}/leads/search"
        query_params = {k: v for k, v in [('term', term), ('fields', fields), ('exact_match', exact_match), ('person_id', person_id), ('organization_id', organization_id), ('include_fields', include_fields), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def lead_labels_get_all(self) -> dict[str, Any]:
        """
        Retrieves a list of all lead labels from the Pipedrive API, allowing users to view and manage the labels used to categorize leads visually.

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            LeadLabels
        """
        url = f"{self.base_url}/leadLabels"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def lead_labels_add_new_label(self, name, color) -> dict[str, Any]:
        """
        Creates a new lead label in Pipedrive with specified name and color.

        Args:
            name (string): The name of the lead label
            color (string): The color of the label. Only a subset of colors can be used.

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            LeadLabels
        """
        request_body = {
            'name': name,
            'color': color,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/leadLabels"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def lead_labels_update_properties(self, id, name=None, color=None) -> dict[str, Any]:
        """
        Updates one or more properties of a lead label using the Pipedrive API, allowing for partial modification of a label with the specified ID.

        Args:
            id (string): id
            name (string): The name of the lead label
            color (string): The color of the label. Only a subset of colors can be used.

        Returns:
            dict[str, Any]: Successful response containing payload in the `data` field

        Tags:
            LeadLabels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'color': color,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/leadLabels/{id}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def lead_labels_delete_label(self, id) -> dict[str, Any]:
        """
        Deletes a specific lead label by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Successful response with id value only. Used in DELETE calls.

        Tags:
            LeadLabels
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/leadLabels/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def lead_sources_get_all(self) -> dict[str, Any]:
        """
        Retrieves a list of available lead sources using the `GET` method at the `/leadSources` path.

        Returns:
            dict[str, Any]: The successful response containing payload in the `data` field.

        Tags:
            LeadSources
        """
        url = f"{self.base_url}/leadSources"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_get_all_teams(self, order_by=None, skip_users=None) -> Any:
        """
        Retrieves a list of legacy teams within an organization using the GET method, allowing for optional sorting by specific fields and excluding user IDs from the response.

        Args:
            order_by (string): The field name to sort returned teams by
            skip_users (number): When enabled, the teams will not include IDs of member users

        Returns:
            Any: The list of team objects

        Tags:
            LegacyTeams
        """
        url = f"{self.base_url}/legacyTeams"
        query_params = {k: v for k, v in [('order_by', order_by), ('skip_users', skip_users)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_add_new_team(self, name, manager_id, description=None, users=None) -> Any:
        """
        Creates a new team within an organization using the Pipedrive API and returns the team details upon successful creation.

        Args:
            name (string): The team name
            manager_id (integer): The team manager ID
            description (string): The team description
            users (array): The list of user IDs

        Returns:
            Any: The team data

        Tags:
            LegacyTeams
        """
        request_body = {
            'description': description,
            'name': name,
            'manager_id': manager_id,
            'users': users,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/legacyTeams"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_get_data(self, id, skip_users=None) -> Any:
        """
        Retrieves data about a specific team identified by its ID, optionally excluding user information, using the Pipedrive Legacy Teams API.

        Args:
            id (string): id
            skip_users (number): When enabled, the teams will not include IDs of member users

        Returns:
            Any: The team data

        Tags:
            LegacyTeams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/legacyTeams/{id}"
        query_params = {k: v for k, v in [('skip_users', skip_users)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_update_team_object(self, id, description=None, name=None, manager_id=None, users=None, active_flag=None, deleted_flag=None) -> Any:
        """
        Updates an existing team with the specified ID using the Pipedrive API, potentially allowing modifications to team details such as name, manager, or members.

        Args:
            id (string): id
            description (string): The team description
            name (string): The team name
            manager_id (integer): The team manager ID
            users (array): The list of user IDs
            active_flag (string): Flag that indicates whether the team is active
            deleted_flag (string): Flag that indicates whether the team is deleted

        Returns:
            Any: The team data

        Tags:
            LegacyTeams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'description': description,
            'name': name,
            'manager_id': manager_id,
            'users': users,
            'active_flag': active_flag,
            'deleted_flag': deleted_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/legacyTeams/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_get_all_users(self, id) -> Any:
        """
        Retrieves the list of user IDs belonging to a specified legacy team by team ID.

        Args:
            id (string): id

        Returns:
            Any: A list of user IDs within a team

        Tags:
            LegacyTeams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/legacyTeams/{id}/users"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_add_users_to_team(self, id, users) -> Any:
        """
        Adds users to an existing team in Pipedrive using the API endpoint "/legacyTeams/{id}/users" with the POST method.

        Args:
            id (string): id
            users (array): The list of user IDs

        Returns:
            Any: A list of user IDs within a team

        Tags:
            LegacyTeams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'users': users,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/legacyTeams/{id}/users"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def legacy_teams_get_user_teams(self, id, order_by=None, skip_users=None) -> Any:
        """
        Retrieves information about the team memberships of a specific user identified by `{id}` using the Pipedrive API, with options to customize the response by sorting teams and excluding user IDs.

        Args:
            id (string): id
            order_by (string): The field name to sort returned teams by
            skip_users (number): When enabled, the teams will not include IDs of member users

        Returns:
            Any: The list of team objects

        Tags:
            LegacyTeams
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/legacyTeams/user/{id}"
        query_params = {k: v for k, v in [('order_by', order_by), ('skip_users', skip_users)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mailbox_get_mail_message(self, id, include_body=None) -> Any:
        """
        Retrieves details of a specific email message from the mailbox, optionally including the full message body.

        Args:
            id (string): id
            include_body (number): Whether to include the full message body or not. `0` = Don't include, `1` = Include.

        Returns:
            Any: The mail messages that are being synced with Pipedrive

        Tags:
            Mailbox
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/mailbox/mailMessages/{id}"
        query_params = {k: v for k, v in [('include_body', include_body)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mailbox_get_mail_threads(self, folder, start=None, limit=None) -> Any:
        """
        Retrieves a list of email threads from a mailbox, filtered by a specified folder, starting from a certain position, and limited to a defined number of results.

        Args:
            folder (string): The type of folder to fetch
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Get mail threads

        Tags:
            Mailbox
        """
        url = f"{self.base_url}/mailbox/mailThreads"
        query_params = {k: v for k, v in [('folder', folder), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mailbox_mark_thread_deleted(self, id) -> Any:
        """
        Deletes a specific mail thread by its ID from the mailbox using the "DELETE" method.

        Args:
            id (string): id

        Returns:
            Any: Marks mail thread as deleted

        Tags:
            Mailbox
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/mailbox/mailThreads/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mailbox_get_mail_thread(self, id) -> Any:
        """
        Retrieves a specific email thread from the mailbox by its ID using the Pipedrive API.

        Args:
            id (string): id

        Returns:
            Any: Get mail threads

        Tags:
            Mailbox
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/mailbox/mailThreads/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def mailbox_get_all_mail_messages(self, id) -> Any:
        """
        Retrieves all email messages within a specified mail thread using the provided thread ID.

        Args:
            id (string): id

        Returns:
            Any: Get mail messages from thread

        Tags:
            Mailbox
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/mailbox/mailThreads/{id}/mailMessages"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def meetings_link_user_provider(self, user_provider_id, user_id, company_id, marketplace_client_id) -> dict[str, Any]:
        """
        Creates user provider links for meetings using the POST method and returns a status message upon success.

        Args:
            user_provider_id (string): Unique identifier linking a user to the installed integration. Generated by the integration. Example: '1e3943c9-6395-462b-b432-1f252c017f3d'.
            user_id (integer): Pipedrive user ID Example: '123'.
            company_id (integer): Pipedrive company ID Example: '456'.
            marketplace_client_id (string): Pipedrive Marketplace client ID of the installed integration Example: '57da5c3c55a82bb4'.

        Returns:
            dict[str, Any]: User provider link was successfully created

        Tags:
            Meetings
        """
        request_body = {
            'user_provider_id': user_provider_id,
            'user_id': user_id,
            'company_id': company_id,
            'marketplace_client_id': marketplace_client_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/meetings/userProviderLinks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def meetings_remove_user_provider_link(self, id) -> dict[str, Any]:
        """
        Deletes a user provider link by the specified ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: User provider link successfully removed

        Tags:
            Meetings
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/meetings/userProviderLinks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_get_all(self, user_id=None, lead_id=None, deal_id=None, person_id=None, org_id=None, start=None, limit=None, sort=None, start_date=None, end_date=None, pinned_to_lead_flag=None, pinned_to_deal_flag=None, pinned_to_organization_flag=None, pinned_to_person_flag=None) -> dict[str, Any]:
        """
        Retrieves a filtered list of notes based on specified query parameters like user, lead, deal, person, organization IDs, date ranges, and pinned statuses.

        Args:
            user_id (integer): The ID of the user whose notes to fetch. If omitted, notes by all users will be returned.
            lead_id (string): The ID of the lead which notes to fetch. If omitted, notes about all leads will be returned.
            deal_id (integer): The ID of the deal which notes to fetch. If omitted, notes about all deals will be returned.
            person_id (integer): The ID of the person whose notes to fetch. If omitted, notes about all persons will be returned.
            org_id (integer): The ID of the organization which notes to fetch. If omitted, notes about all organizations will be returned.
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `content`, `add_time`, `update_time`.
            start_date (string): The date in format of YYYY-MM-DD from which notes to fetch
            end_date (string): The date in format of YYYY-MM-DD until which notes to fetch to
            pinned_to_lead_flag (number): If set, the results are filtered by note to lead pinning state
            pinned_to_deal_flag (number): If set, the results are filtered by note to deal pinning state
            pinned_to_organization_flag (number): If set, the results are filtered by note to organization pinning state
            pinned_to_person_flag (number): If set, the results are filtered by note to person pinning state

        Returns:
            dict[str, Any]: Get all notes

        Tags:
            Notes
        """
        url = f"{self.base_url}/notes"
        query_params = {k: v for k, v in [('user_id', user_id), ('lead_id', lead_id), ('deal_id', deal_id), ('person_id', person_id), ('org_id', org_id), ('start', start), ('limit', limit), ('sort', sort), ('start_date', start_date), ('end_date', end_date), ('pinned_to_lead_flag', pinned_to_lead_flag), ('pinned_to_deal_flag', pinned_to_deal_flag), ('pinned_to_organization_flag', pinned_to_organization_flag), ('pinned_to_person_flag', pinned_to_person_flag)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_create_note(self, content, lead_id=None, deal_id=None, person_id=None, org_id=None, user_id=None, add_time=None, pinned_to_lead_flag=None, pinned_to_deal_flag=None, pinned_to_organization_flag=None, pinned_to_person_flag=None) -> dict[str, Any]:
        """
        Creates a new note entry via the specified endpoint and returns a success status upon completion.

        Args:
            content (string): The content of the note in HTML format. Subject to sanitization on the back-end.
            lead_id (string): The ID of the lead the note will be attached to. This property is required unless one of (`deal_id/person_id/org_id`) is specified.
            deal_id (integer): The ID of the deal the note will be attached to. This property is required unless one of (`lead_id/person_id/org_id`) is specified.
            person_id (integer): The ID of the person this note will be attached to. This property is required unless one of (`deal_id/lead_id/org_id`) is specified.
            org_id (integer): The ID of the organization this note will be attached to. This property is required unless one of (`deal_id/lead_id/person_id`) is specified.
            user_id (integer): The ID of the user who will be marked as the author of the note. Only an admin can change the author.
            add_time (string): The optional creation date & time of the note in UTC. Can be set in the past or in the future. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS
            pinned_to_lead_flag (string): If set, the results are filtered by note to lead pinning state (`lead_id` is also required)
            pinned_to_deal_flag (string): If set, the results are filtered by note to deal pinning state (`deal_id` is also required)
            pinned_to_organization_flag (string): If set, the results are filtered by note to organization pinning state (`org_id` is also required)
            pinned_to_person_flag (string): If set, the results are filtered by note to person pinning state (`person_id` is also required)

        Returns:
            dict[str, Any]: Add, update or get a note

        Tags:
            Notes
        """
        request_body = {
            'content': content,
            'lead_id': lead_id,
            'deal_id': deal_id,
            'person_id': person_id,
            'org_id': org_id,
            'user_id': user_id,
            'add_time': add_time,
            'pinned_to_lead_flag': pinned_to_lead_flag,
            'pinned_to_deal_flag': pinned_to_deal_flag,
            'pinned_to_organization_flag': pinned_to_organization_flag,
            'pinned_to_person_flag': pinned_to_person_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/notes"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_delete_note(self, id) -> dict[str, Any]:
        """
        Deletes a note with the specified {id} from the collection of notes using the DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete a note

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/notes/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves a specific note by its ID using the "GET" method at "/notes/{id}".

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Add, update or get a note

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/notes/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_update_note(self, id, content=None, lead_id=None, deal_id=None, person_id=None, org_id=None, user_id=None, add_time=None, pinned_to_lead_flag=None, pinned_to_deal_flag=None, pinned_to_organization_flag=None, pinned_to_person_flag=None) -> dict[str, Any]:
        """
        Updates an existing note resource identified by the path ID and returns the updated data.

        Args:
            id (string): id
            content (string): The content of the note in HTML format. Subject to sanitization on the back-end.
            lead_id (string): The ID of the lead the note will be attached to
            deal_id (integer): The ID of the deal the note will be attached to
            person_id (integer): The ID of the person the note will be attached to
            org_id (integer): The ID of the organization the note will be attached to
            user_id (integer): The ID of the user who will be marked as the author of the note. Only an admin can change the author.
            add_time (string): The optional creation date & time of the note in UTC. Can be set in the past or in the future. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS
            pinned_to_lead_flag (string): If set, the results are filtered by note to lead pinning state (`lead_id` is also required)
            pinned_to_deal_flag (string): If set, the results are filtered by note to deal pinning state (`deal_id` is also required)
            pinned_to_organization_flag (string): If set, the results are filtered by note to organization pinning state (`org_id` is also required)
            pinned_to_person_flag (string): If set, the results are filtered by note to person pinning state (`person_id` is also required)

        Returns:
            dict[str, Any]: Add, update or get a note

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'content': content,
            'lead_id': lead_id,
            'deal_id': deal_id,
            'person_id': person_id,
            'org_id': org_id,
            'user_id': user_id,
            'add_time': add_time,
            'pinned_to_lead_flag': pinned_to_lead_flag,
            'pinned_to_deal_flag': pinned_to_deal_flag,
            'pinned_to_organization_flag': pinned_to_organization_flag,
            'pinned_to_person_flag': pinned_to_person_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/notes/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_get_all_comments(self, id, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves comments for a specific note with pagination support using path and query parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: Get all comments

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/notes/{id}/comments"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_add_new_comment(self, id, content) -> dict[str, Any]:
        """
        Adds a new comment to a note specified by its ID using the POST method.

        Args:
            id (string): id
            content (string): The content of the comment in HTML format. Subject to sanitization on the back-end.

        Returns:
            dict[str, Any]: Add, update or get a comment

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'content': content,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/notes/{id}/comments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_get_comment_details(self, id, commentId) -> dict[str, Any]:
        """
        Retrieves a specific comment from a note by its ID and comment ID using the API.

        Args:
            id (string): id
            commentId (string): commentId

        Returns:
            dict[str, Any]: Add, update or get a comment

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'")
        url = f"{self.base_url}/notes/{id}/comments/{commentId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_update_comment(self, id, commentId, content) -> dict[str, Any]:
        """
        Updates a specific comment for a note using the PUT method, allowing complete replacement of the comment's content identified by the note ID and comment ID.

        Args:
            id (string): id
            commentId (string): commentId
            content (string): The content of the comment in HTML format. Subject to sanitization on the back-end.

        Returns:
            dict[str, Any]: Add, update or get a comment

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'")
        request_body = {
            'content': content,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/notes/{id}/comments/{commentId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notes_delete_comment(self, id, commentId) -> dict[str, Any]:
        """
        Deletes a specific comment from a note using the provided comment identifier and note ID.

        Args:
            id (string): id
            commentId (string): commentId

        Returns:
            dict[str, Any]: Delete a comment

        Tags:
            Notes
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if commentId is None:
            raise ValueError("Missing required parameter 'commentId'")
        url = f"{self.base_url}/notes/{id}/comments/{commentId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def note_fields_get_all_note_fields(self) -> Any:
        """
        Retrieves a list of note fields using the API endpoint at "/noteFields" via the GET method.

        Returns:
            Any: Success

        Tags:
            NoteFields
        """
        url = f"{self.base_url}/noteFields"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_delete_multiple_bulk(self, ids) -> dict[str, Any]:
        """
        Deletes one or more organizations identified by their IDs using the "DELETE" method on the "/organizations" path.

        Args:
            ids (string): The comma-separated IDs that will be deleted

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        url = f"{self.base_url}/organizations"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_get_all(self, user_id=None, filter_id=None, first_char=None, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of organizations filtered by user ID, filter criteria, alphabetical starting character, pagination settings, and sorting parameters.

        Args:
            user_id (integer): If supplied, only organizations owned by the given user will be returned. However, `filter_id` takes precedence over `user_id` when both are supplied.
            filter_id (integer): The ID of the filter to use
            first_char (string): If supplied, only organizations whose name starts with the specified letter will be returned (case-insensitive)
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        url = f"{self.base_url}/organizations"
        query_params = {k: v for k, v in [('user_id', user_id), ('filter_id', filter_id), ('first_char', first_char), ('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_add_new_organization(self, name, add_time=None, owner_id=None, label=None, visible_to=None) -> Any:
        """
        Creates a new organization using the API and returns a success status upon creation.

        Args:
            name (string): The name of the organization
            add_time (string): The optional creation date & time of the organization in UTC. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS
            owner_id (integer): The ID of the user who will be marked as the owner of this organization. When omitted, the authorized user ID will be used.
            label (integer): The ID of the label.
            visible_to (string): The visibility of the organization. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        request_body = {
            'name': name,
            'add_time': add_time,
            'owner_id': owner_id,
            'label': label,
            'visible_to': visible_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_all_organizations(self, cursor=None, limit=None, since=None, until=None, owner_id=None, first_char=None) -> dict[str, Any]:
        """
        Retrieves a list of organizations with optional filtering by owner, time range, and alphabetical criteria[1][2][5].

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed. Example: '100'.
            since (string): The time boundary that points to the start of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            until (string): The time boundary that points to the end of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            owner_id (integer): If supplied, only organizations owned by the given user will be returned
            first_char (string): If supplied, only organizations whose name starts with the specified letter will be returned (case-insensitive)

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        url = f"{self.base_url}/organizations/collection"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('since', since), ('until', until), ('owner_id', owner_id), ('first_char', first_char)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_search_by_criteria(self, term, fields=None, exact_match=None, start=None, limit=None) -> Any:
        """
        Retrieves a list of organizations based on a search term, allowing for customization by specifying fields, exact match, and pagination parameters using the "GET" method.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all of them. Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        url = f"{self.base_url}/organizations/search"
        query_params = {k: v for k, v in [('term', term), ('fields', fields), ('exact_match', exact_match), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_delete_marked_organization(self, id) -> dict[str, Any]:
        """
        Deletes an organization and disassociates all members from it using the specified organization ID in the path.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_get_details(self, id) -> Any:
        """
        Retrieves details of a specific organization by its unique identifier.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_update_properties(self, id, name=None, owner_id=None, label=None, visible_to=None) -> Any:
        """
        Updates the specified organization's details using the provided ID and returns a success status upon completion.

        Args:
            id (string): id
            name (string): The name of the organization
            owner_id (integer): The ID of the user who will be marked as the owner of this organization. When omitted, the authorized user ID will be used.
            label (integer): The ID of the label.
            visible_to (string): The visibility of the organization. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'owner_id': owner_id,
            'label': label,
            'visible_to': visible_to,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_activities(self, id, start=None, limit=None, done=None, exclude=None) -> Any:
        """
        Retrieves a filtered list of activities for an organization including optional parameters for start time, result limits, completion status, and exclusions.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            done (number): Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted returns both Done and Not done activities.
            exclude (string): A comma-separated string of activity IDs to exclude from result

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/activities"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('done', done), ('exclude', exclude)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_deals(self, id, start=None, limit=None, status=None, sort=None, only_primary_association=None) -> Any:
        """
        Retrieves a list of deals associated with a specific organization using the Pipedrive API, allowing for pagination and filtering by status.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            status (string): Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).
            only_primary_association (number): If set, only deals that are directly associated to the organization are fetched. If not set (default), all deals are fetched that are either directly or indirectly related to the organization. Indirect relations include relations through custom, organization-type fields and through persons of the given organization.

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/deals"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('status', status), ('sort', sort), ('only_primary_association', only_primary_association)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_attached_files(self, id, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of files associated with a specific organization, optionally filtered, paginated, and sorted by query parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `product_id`, `add_time`, `update_time`, `file_name`, `file_type`, `file_size`, `comment`.

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/files"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_updates_about(self, id, start=None, limit=None, all_changes=None, items=None) -> Any:
        """
        Retrieves flow-related data for a specific organization, optionally filtered by time range, item type, and pagination parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            all_changes (string): Whether to show custom field updates or not. 1 = Include custom field changes. If omitted, returns changes without custom field updates.
            items (string): A comma-separated string for filtering out item specific updates. (Possible values - activity, plannedActivity, note, file, change, deal, follower, participant, mailMessage, mailMessageWithAttachment, invoice, activityFile, document).

        Returns:
            Any: Get the organization updates

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/flow"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('all_changes', all_changes), ('items', items)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_followers(self, id) -> dict[str, Any]:
        """
        Retrieves a list of followers for an organization with the specified ID using the GitHub API.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/followers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_add_follower(self, id, user_id) -> dict[str, Any]:
        """
        Adds a follower to a GitHub organization using the POST method at the "/organizations/{id}/followers" endpoint.

        Args:
            id (string): id
            user_id (integer): The ID of the user

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'user_id': user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{id}/followers"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_delete_follower(self, id, follower_id) -> dict[str, Any]:
        """
        Removes a follower from an organization with the specified ID and follower ID using the GitHub API.

        Args:
            id (string): id
            follower_id (string): follower_id

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if follower_id is None:
            raise ValueError("Missing required parameter 'follower_id'")
        url = f"{self.base_url}/organizations/{id}/followers/{follower_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_mail_messages(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of mail messages associated with an organization identified by the specified ID, allowing pagination through the start and limit parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/mailMessages"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_merge_two(self, id, merge_with_id) -> dict[str, Any]:
        """
        Configures merge settings for a GitHub organization using the provided organization ID and returns a success status upon completion.

        Args:
            id (string): id
            merge_with_id (integer): The ID of the organization that the organization will be merged with

        Returns:
            dict[str, Any]: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'merge_with_id': merge_with_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{id}/merge"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_permitted_users(self, id) -> Any:
        """
        Retrieves a list of permitted users for a specified organization using the "GET" method at the "/organizations/{id}/permittedUsers" endpoint.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/permittedUsers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organizations_list_persons(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of persons associated with an organization, identified by the organization ID, with optional pagination using start and limit parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Organizations
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizations/{id}/persons"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_get_all_fields(self, start=None, limit=None) -> Any:
        """
        Retrieves a list of organization fields, including custom fields, using the "GET" method at "/organizationFields", supporting query parameters like "start" and "limit" for pagination.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        url = f"{self.base_url}/organizationFields"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_add_new_field(self, name, field_type, options=None, add_visible_flag=True) -> Any:
        """
        Adds a new organization field using the POST method at the "/organizationFields" path, allowing the creation of custom fields for organizational data management.

        Args:
            name (string): The name of the field
            field_type (string): The type of the field<table><tr><th>Value</th><th>Description</th></tr><tr><td>`address`</td><td>Address field (has multiple subfields, autocompleted by Google Maps)</td></tr><tr><td>`date`</td><td>Date (format YYYY-MM-DD)</td></tr><tr><td>`daterange`</td><td>Date-range field (has a start date and end date value, both YYYY-MM-DD)</td></tr><tr><td>`double`</td><td>Numeric value</td></tr><tr><td>`enum`</td><td>Options field with a single possible chosen option</td></tr><tr></tr><tr><td>`monetary`</td><td>Monetary field (has a numeric value and a currency value)</td></tr><tr><td>`org`</td><td>Organization field (contains an organization ID which is stored on the same account)</td></tr><tr><td>`people`</td><td>Person field (contains a person ID which is stored on the same account)</td></tr><tr><td>`phone`</td><td>Phone field (up to 255 numbers and/or characters)</td></tr><tr><td>`set`</td><td>Options field with a possibility of having multiple chosen options</td></tr><tr><td>`text`</td><td>Long text (up to 65k characters)</td></tr><tr><td>`time`</td><td>Time field (format HH:MM:SS)</td></tr><tr><td>`timerange`</td><td>Time-range field (has a start time and end time value, both HH:MM:SS)</td></tr><tr><td>`user`</td><td>User field (contains a user ID of another Pipedrive user)</td></tr><tr><td>`varchar`</td><td>Text (up to 255 characters)</td></tr><tr><td>`varchar_auto`</td><td>Autocomplete text (up to 255 characters)</td></tr><tr><td>`visible_to`</td><td>System field that keeps item's visibility setting</td></tr></table>
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. Example: `[{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in the 'add new' modal or not (both in the web and mobile app)

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
            'field_type': field_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizationFields"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_delete_multiple_bulk(self, ids) -> Any:
        """
        Deletes specified organization fields by their IDs and returns a success status upon completion.

        Args:
            ids (string): The comma-separated field IDs to delete

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        url = f"{self.base_url}/organizationFields"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_get_specific_field(self, id) -> Any:
        """
        Retrieves data about a specific organization field based on the provided field ID using the Pipedrive API.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizationFields/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_mark_as_deleted(self, id) -> Any:
        """
        Deletes an organization field identified by the provided ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizationFields/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_fields_update_field(self, id, name=None, options=None, add_visible_flag=True) -> Any:
        """
        Updates an existing organization field by ID and returns the updated field data upon success.

        Args:
            id (string): id
            name (string): The name of the field
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. All active items must be supplied and already existing items must have their ID supplied. New items only require a label. Example: `[{"id":123,"label":"Existing Item"},{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in 'add new' modal or not (both in web and mobile app)

        Returns:
            Any: Success

        Tags:
            OrganizationFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizationFields/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_relationships_get_all_relationships(self, org_id) -> Any:
        """
        Retrieves organization relationships based on the specified organization ID.

        Args:
            org_id (integer): The ID of the organization to get relationships for

        Returns:
            Any: Success

        Tags:
            OrganizationRelationships
        """
        url = f"{self.base_url}/organizationRelationships"
        query_params = {k: v for k, v in [('org_id', org_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_relationships_create_new_relationship(self, type, rel_owner_org_id, rel_linked_org_id, org_id=None) -> Any:
        """
        Creates an organization relationship and returns a success confirmation upon completion.

        Args:
            type (string): The type of organization relationship
            rel_owner_org_id (integer): The owner of the relationship. If type is `parent`, then the owner is the parent and the linked organization is the daughter.
            rel_linked_org_id (integer): The linked organization in the relationship. If type is `parent`, then the linked organization is the daughter.
            org_id (integer): The ID of the base organization for the returned calculated values

        Returns:
            Any: Success

        Tags:
            OrganizationRelationships
        """
        request_body = {
            'org_id': org_id,
            'type': type,
            'rel_owner_org_id': rel_owner_org_id,
            'rel_linked_org_id': rel_linked_org_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizationRelationships"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_relationships_delete_by_id(self, id) -> Any:
        """
        Deletes a specific organization relationship by its ID using the GitHub API.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            OrganizationRelationships
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizationRelationships/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_relationships_get_by_id(self, id, org_id=None) -> Any:
        """
        Retrieves a specific organization relationship by its ID along with calculated values for the base organization.

        Args:
            id (string): id
            org_id (integer): The ID of the base organization for the returned calculated values

        Returns:
            Any: Success

        Tags:
            OrganizationRelationships
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/organizationRelationships/{id}"
        query_params = {k: v for k, v in [('org_id', org_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def organization_relationships_update_and_return(self, id, org_id=None, type=None, rel_owner_org_id=None, rel_linked_org_id=None) -> Any:
        """
        Updates an organizational relationship identified by `{id}` using the GitHub API and returns a success status upon completion.

        Args:
            id (string): id
            org_id (integer): The ID of the base organization for the returned calculated values
            type (string): The type of organization relationship
            rel_owner_org_id (integer): The owner of this relationship. If type is `parent`, then the owner is the parent and the linked organization is the daughter.
            rel_linked_org_id (integer): The linked organization in this relationship. If type is `parent`, then the linked organization is the daughter.

        Returns:
            Any: Success

        Tags:
            OrganizationRelationships
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'org_id': org_id,
            'type': type,
            'rel_owner_org_id': rel_owner_org_id,
            'rel_linked_org_id': rel_linked_org_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizationRelationships/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def permission_sets_get_all(self, app=None) -> Any:
        """
        Retrieves all permission sets for a specified application using query parameters.

        Args:
            app (string): The app to filter the permission sets by

        Returns:
            Any: Get all permissions

        Tags:
            PermissionSets
        """
        url = f"{self.base_url}/permissionSets"
        query_params = {k: v for k, v in [('app', app)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def permission_sets_get_one(self, id) -> Any:
        """
        Retrieves a specific permission set by its ID from the collection of permission sets using the GET method, returning detailed information about the set.

        Args:
            id (string): id

        Returns:
            Any: The permission set of a specific user ID

        Tags:
            PermissionSets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/permissionSets/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def permission_sets_list_assignments(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a paginated list of assignments associated with a specific permission set using the provided ID and query parameters for pagination.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: The assignments of a specific user ID

        Tags:
            PermissionSets
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/permissionSets/{id}/assignments"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_delete_multiple_bulk(self, ids) -> Any:
        """
        Deletes one or more persons from a database by specifying their IDs in the query parameters.

        Args:
            ids (string): The comma-separated IDs that will be deleted

        Returns:
            Any: Success

        Tags:
            Persons
        """
        url = f"{self.base_url}/persons"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_all_persons(self, user_id=None, filter_id=None, first_char=None, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of persons based on specified parameters such as user ID, filter ID, first character, start index, limit, and sort order.

        Args:
            user_id (integer): If supplied, only persons owned by the given user will be returned. However, `filter_id` takes precedence over `user_id` when both are supplied.
            filter_id (integer): The ID of the filter to use
            first_char (string): If supplied, only persons whose name starts with the specified letter will be returned (case-insensitive)
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

        Returns:
            Any: Success

        Tags:
            Persons
        """
        url = f"{self.base_url}/persons"
        query_params = {k: v for k, v in [('user_id', user_id), ('filter_id', filter_id), ('first_char', first_char), ('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_create_new_person(self, name, owner_id=None, org_id=None, email=None, phone=None, label=None, visible_to=None, marketing_status=None, add_time=None) -> Any:
        """
        Creates a new person record in the system and returns the created resource.

        Args:
            name (string): The name of the person
            owner_id (integer): The ID of the user who will be marked as the owner of this person. When omitted, the authorized user ID will be used.
            org_id (integer): The ID of the organization this person will belong to
            email (array): An email address as a string or an array of email objects related to the person. The structure of the array is as follows: `[{ "value": "mail@example.com", "primary": "true", "label": "main" }]`. Please note that only `value` is required.
            phone (array): A phone number supplied as a string or an array of phone objects related to the person. The structure of the array is as follows: `[{ "value": "12345", "primary": "true", "label": "mobile" }]`. Please note that only `value` is required.
            label (integer): The ID of the label.
            visible_to (string): The visibility of the person. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            marketing_status (string): If the person does not have a valid email address, then the marketing status is **not set** and `no_consent` is returned for the `marketing_status` value when the new person is created. If the change is forbidden, the status will remain unchanged for every call that tries to modify the marketing status. Please be aware that it is only allowed **once** to change the marketing status from an old status to a new one.<table><tr><th>Value</th><th>Description</th></tr><tr><td>`no_consent`</td><td>The customer has not given consent to receive any marketing communications</td></tr><tr><td>`unsubscribed`</td><td>The customers have unsubscribed from ALL marketing communications</td></tr><tr><td>`subscribed`</td><td>The customers are subscribed and are counted towards marketing caps</td></tr><tr><td>`archived`</td><td>The customers with `subscribed` status can be moved to `archived` to save consent, but they are not paid for</td></tr></table>
            add_time (string): The optional creation date & time of the person in UTC. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS

        Returns:
            Any: Success

        Tags:
            Persons
        """
        request_body = {
            'name': name,
            'owner_id': owner_id,
            'org_id': org_id,
            'email': email,
            'phone': phone,
            'label': label,
            'visible_to': visible_to,
            'marketing_status': marketing_status,
            'add_time': add_time,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/persons"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_get_all(self, cursor=None, limit=None, since=None, until=None, owner_id=None, first_char=None) -> dict[str, Any]:
        """
        Retrieves a collection of persons based on specified criteria such as cursor, limit, date range, owner ID, and first character, using the GET method at the "/persons/collection" endpoint.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Please note that a maximum value of 500 is allowed. Example: '100'.
            since (string): The time boundary that points to the start of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            until (string): The time boundary that points to the end of the range of data. Datetime in ISO 8601 format. E.g. 2022-11-01 08:55:59. Operates on the `update_time` field.
            owner_id (integer): If supplied, only persons owned by the given user will be returned
            first_char (string): If supplied, only persons whose name starts with the specified letter will be returned (case-insensitive)

        Returns:
            dict[str, Any]: Success

        Tags:
            Persons
        """
        url = f"{self.base_url}/persons/collection"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('since', since), ('until', until), ('owner_id', owner_id), ('first_char', first_char)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_search_by_criteria(self, term, fields=None, exact_match=None, organization_id=None, include_fields=None, start=None, limit=None) -> Any:
        """
        Searches for persons based on a given term, allowing filtering by fields, exact match, organization ID, and additional options to customize the search results, using the GET method at the "/persons/search" endpoint.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all of them. Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            organization_id (integer): Will filter persons by the provided organization ID. The upper limit of found persons associated with the organization is 2000.
            include_fields (string): Supports including optional fields in the results which are not provided by default
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Persons
        """
        url = f"{self.base_url}/persons/search"
        query_params = {k: v for k, v in [('term', term), ('fields', fields), ('exact_match', exact_match), ('organization_id', organization_id), ('include_fields', include_fields), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_mark_as_deleted(self, id) -> Any:
        """
        Deletes a specific person by ID and returns a success status upon completion.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_get_person_details(self, id) -> Any:
        """
        Retrieves details of a specific person by their unique identifier.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_update_properties(self, id, name=None, owner_id=None, org_id=None, email=None, phone=None, label=None, visible_to=None, marketing_status=None, add_time=None) -> Any:
        """
        Updates a person's details at the specified ID using the PUT method, replacing the entire existing record with the new data provided.

        Args:
            id (string): id
            name (string): The name of the person
            owner_id (integer): The ID of the user who will be marked as the owner of this person. When omitted, the authorized user ID will be used.
            org_id (integer): The ID of the organization this person will belong to
            email (array): An email address as a string or an array of email objects related to the person. The structure of the array is as follows: `[{ "value": "mail@example.com", "primary": "true", "label": "main" }]`. Please note that only `value` is required.
            phone (array): A phone number supplied as a string or an array of phone objects related to the person. The structure of the array is as follows: `[{ "value": "12345", "primary": "true", "label": "mobile" }]`. Please note that only `value` is required.
            label (integer): The ID of the label.
            visible_to (string): The visibility of the person. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width:40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            marketing_status (string): If the person does not have a valid email address, then the marketing status is **not set** and `no_consent` is returned for the `marketing_status` value when the new person is created. If the change is forbidden, the status will remain unchanged for every call that tries to modify the marketing status. Please be aware that it is only allowed **once** to change the marketing status from an old status to a new one.<table><tr><th>Value</th><th>Description</th></tr><tr><td>`no_consent`</td><td>The customer has not given consent to receive any marketing communications</td></tr><tr><td>`unsubscribed`</td><td>The customers have unsubscribed from ALL marketing communications</td></tr><tr><td>`subscribed`</td><td>The customers are subscribed and are counted towards marketing caps</td></tr><tr><td>`archived`</td><td>The customers with `subscribed` status can be moved to `archived` to save consent, but they are not paid for</td></tr></table>
            add_time (string): The optional creation date & time of the person in UTC. Requires admin user API token. Format: YYYY-MM-DD HH:MM:SS

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'owner_id': owner_id,
            'org_id': org_id,
            'email': email,
            'phone': phone,
            'label': label,
            'visible_to': visible_to,
            'marketing_status': marketing_status,
            'add_time': add_time,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/persons/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_activities(self, id, start=None, limit=None, done=None, exclude=None) -> Any:
        """
        Retrieves a list of activities for a person identified by `{id}`, allowing optional filtering by start time, activity limit, completion status, and exclusions.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            done (number): Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted, returns both Done and Not done activities.
            exclude (string): A comma-separated string of activity IDs to exclude from result

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/activities"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('done', done), ('exclude', exclude)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_deals(self, id, start=None, limit=None, status=None, sort=None) -> Any:
        """
        Retrieves a list of deals associated with a person, filtered by status, sorted as specified, and paginated based on the provided start and limit parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            status (string): Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys).

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/deals"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('status', status), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_person_files(self, id, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of files associated with a specific person ID, optionally filtered by start date, size limit, and sorting parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field names and sorting mode separated by a comma (`field_name_1 ASC`, `field_name_2 DESC`). Only first-level field keys are supported (no nested keys). Supported fields: `id`, `user_id`, `deal_id`, `person_id`, `org_id`, `product_id`, `add_time`, `update_time`, `file_name`, `file_type`, `file_size`, `comment`.

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/files"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_updates_about(self, id, start=None, limit=None, all_changes=None, items=None) -> Any:
        """
        Retrieves a workflow or process flow associated with a specific person ID, optionally filtered by start time, result limit, inclusion of all changes, and specific items.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            all_changes (string): Whether to show custom field updates or not. 1 = Include custom field changes. If omitted returns changes without custom field updates.
            items (string): A comma-separated string for filtering out item specific updates. (Possible values - call, activity, plannedActivity, change, note, deal, file, dealChange, personChange, organizationChange, follower, dealFollower, personFollower, organizationFollower, participant, comment, mailMessage, mailMessageWithAttachment, invoice, document, marketing_campaign_stat, marketing_status_change).

        Returns:
            Any: Get the person updates

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/flow"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('all_changes', all_changes), ('items', items)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_followers(self, id) -> Any:
        """
        Retrieves a list of followers associated with the specified person ID.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/followers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_add_follower(self, id, user_id) -> Any:
        """
        Adds followers to a person with the specified ID using the API.

        Args:
            id (string): id
            user_id (integer): The ID of the user

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'user_id': user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/persons/{id}/followers"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_delete_follower(self, id, follower_id) -> Any:
        """
        Removes a specific follower from a person's followers list using the "DELETE" method.

        Args:
            id (string): id
            follower_id (string): follower_id

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if follower_id is None:
            raise ValueError("Missing required parameter 'follower_id'")
        url = f"{self.base_url}/persons/{id}/followers/{follower_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_mail_messages(self, id, start=None, limit=None) -> Any:
        """
        Retrieves mail messages associated with a specific person ID, with pagination support via start and limit parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/mailMessages"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_merge_two(self, id, merge_with_id) -> Any:
        """
        Merges user data by updating the specified person's record using the provided ID in the path.

        Args:
            id (string): id
            merge_with_id (integer): The ID of the person that will not be overwritten. This person’s data will be prioritized in case of conflict with the other person.

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'merge_with_id': merge_with_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/persons/{id}/merge"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list_permitted_users(self, id) -> Any:
        """
        Retrieves a list of users permitted to access or interact with the specified person's data or resources.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/permittedUsers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()



    def persons_list_products(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of products associated with a person identified by their ID, with optional filtering by start index and limit.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Persons
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/persons/{id}/products"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_get_all_fields(self, start=None, limit=None) -> Any:
        """
        Retrieves data about all person fields associated with the authorized user's company using the Pipedrive API, returning a schema that includes custom fields.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        url = f"{self.base_url}/personFields"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_add_new_field(self, name, field_type, options=None, add_visible_flag=True) -> Any:
        """
        Creates or updates person field definitions in the Pipedrive API, returning a success status upon completion.

        Args:
            name (string): The name of the field
            field_type (string): The type of the field<table><tr><th>Value</th><th>Description</th></tr><tr><td>`address`</td><td>Address field (has multiple subfields, autocompleted by Google Maps)</td></tr><tr><td>`date`</td><td>Date (format YYYY-MM-DD)</td></tr><tr><td>`daterange`</td><td>Date-range field (has a start date and end date value, both YYYY-MM-DD)</td></tr><tr><td>`double`</td><td>Numeric value</td></tr><tr><td>`enum`</td><td>Options field with a single possible chosen option</td></tr><tr></tr><tr><td>`monetary`</td><td>Monetary field (has a numeric value and a currency value)</td></tr><tr><td>`org`</td><td>Organization field (contains an organization ID which is stored on the same account)</td></tr><tr><td>`people`</td><td>Person field (contains a person ID which is stored on the same account)</td></tr><tr><td>`phone`</td><td>Phone field (up to 255 numbers and/or characters)</td></tr><tr><td>`set`</td><td>Options field with a possibility of having multiple chosen options</td></tr><tr><td>`text`</td><td>Long text (up to 65k characters)</td></tr><tr><td>`time`</td><td>Time field (format HH:MM:SS)</td></tr><tr><td>`timerange`</td><td>Time-range field (has a start time and end time value, both HH:MM:SS)</td></tr><tr><td>`user`</td><td>User field (contains a user ID of another Pipedrive user)</td></tr><tr><td>`varchar`</td><td>Text (up to 255 characters)</td></tr><tr><td>`varchar_auto`</td><td>Autocomplete text (up to 255 characters)</td></tr><tr><td>`visible_to`</td><td>System field that keeps item's visibility setting</td></tr></table>
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. Example: `[{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in the 'add new' modal or not (both in the web and mobile app)

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
            'field_type': field_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/personFields"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_delete_multiple_bulk(self, ids) -> Any:
        """
        Deletes one or more person fields in Pipedrive by specifying their IDs using the `ids` parameter in the API request.

        Args:
            ids (string): The comma-separated field IDs to delete

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        url = f"{self.base_url}/personFields"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_get_specific_field(self, id) -> Any:
        """
        Retrieves specific details about a person field using the "GET" method at the path "/personFields/{id}".

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/personFields/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_mark_as_deleted(self, id) -> Any:
        """
        Deletes a custom person field in Pipedrive using the specified field ID.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/personFields/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def person_fields_update_field(self, id, name=None, options=None, add_visible_flag=True) -> Any:
        """
        Updates a specific person's fields identified by `{id}` using the PUT method.

        Args:
            id (string): id
            name (string): The name of the field
            options (array): When `field_type` is either set or enum, possible options must be supplied as a JSON-encoded sequential array of objects. All active items must be supplied and already existing items must have their ID supplied. New items only require a label. Example: `[{"id":123,"label":"Existing Item"},{"label":"New Item"}]`
            add_visible_flag (boolean): Whether the field is available in 'add new' modal or not (both in web and mobile app)

        Returns:
            Any: Success

        Tags:
            PersonFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'options': options,
            'add_visible_flag': add_visible_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/personFields/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_get_all(self) -> dict[str, Any]:
        """
        Retrieves a list of pipelines and returns them in the response.

        Returns:
            dict[str, Any]: Get all pipelines

        Tags:
            Pipelines
        """
        url = f"{self.base_url}/pipelines"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_create_new_pipeline(self, name, deal_probability=None, order_nr=None, active=None) -> dict[str, Any]:
        """
        Creates a new pipeline using the POST method and returns a response upon successful creation.

        Args:
            name (string): The name of the pipeline
            deal_probability (string): Whether deal probability is disabled or enabled for this pipeline
            order_nr (integer): Defines the order of pipelines. First order (`order_nr=0`) is the default pipeline.
            active (string): Whether this pipeline will be made inactive (hidden) or active

        Returns:
            dict[str, Any]: Add pipeline

        Tags:
            Pipelines
        """
        request_body = {
            'name': name,
            'deal_probability': deal_probability,
            'order_nr': order_nr,
            'active': active,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pipelines"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_delete_pipeline(self, id) -> dict[str, Any]:
        """
        Deletes a pipeline with the specified ID using the DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete pipeline

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pipelines/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_get_one_pipeline_summary(self, id, totals_convert_currency=None) -> dict[str, Any]:
        """
        Retrieves details for a specific pipeline identified by its ID, optionally converting totals to a specified currency.

        Args:
            id (string): id
            totals_convert_currency (string): The 3-letter currency code of any of the supported currencies. When supplied, `per_stages_converted` is returned in `deals_summary` which contains the currency-converted total amounts in the given currency per each stage. You may also set this parameter to `default_currency` in which case users default currency is used.

        Returns:
            dict[str, Any]: Get pipeline

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pipelines/{id}"
        query_params = {k: v for k, v in [('totals_convert_currency', totals_convert_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_update_properties(self, id, name=None, deal_probability=None, order_nr=None, active=None) -> dict[str, Any]:
        """
        Updates a pipeline by its ID using the specified data and returns a successful response upon completion.

        Args:
            id (string): id
            name (string): The name of the pipeline
            deal_probability (string): Whether deal probability is disabled or enabled for this pipeline
            order_nr (integer): Defines the order of pipelines. First order (`order_nr=0`) is the default pipeline.
            active (string): Whether this pipeline will be made inactive (hidden) or active

        Returns:
            dict[str, Any]: Edit pipeline

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'deal_probability': deal_probability,
            'order_nr': order_nr,
            'active': active,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/pipelines/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_get_conversion_statistics(self, id, start_date, end_date, user_id=None) -> dict[str, Any]:
        """
        Retrieves pipeline conversion statistics (e.g., rates or metrics) for a specified pipeline ID, filtered by date range and/or user ID.

        Args:
            id (string): id
            start_date (string): The start of the period. Date in format of YYYY-MM-DD.
            end_date (string): The end of the period. Date in format of YYYY-MM-DD.
            user_id (integer): The ID of the user who's pipeline metrics statistics to fetch. If omitted, the authorized user will be used.

        Returns:
            dict[str, Any]: Get pipeline deals conversion rates

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pipelines/{id}/conversion_statistics"
        query_params = {k: v for k, v in [('start_date', start_date), ('end_date', end_date), ('user_id', user_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_list_deals(self, id, filter_id=None, user_id=None, everyone=None, stage_id=None, start=None, limit=None, get_summary=None, totals_convert_currency=None) -> dict[str, Any]:
        """
        Retrieves deals in a specific pipeline across all stages, optionally filtered by user, stage, or custom criteria, and supports pagination and summary conversion.

        Args:
            id (string): id
            filter_id (integer): If supplied, only deals matching the given filter will be returned
            user_id (integer): If supplied, `filter_id` will not be considered and only deals owned by the given user will be returned. If omitted, deals owned by the authorized user will be returned.
            everyone (number): If supplied, `filter_id` and `user_id` will not be considered – instead, deals owned by everyone will be returned
            stage_id (integer): If supplied, only deals within the given stage will be returned
            start (integer): Pagination start
            limit (integer): Items shown per page
            get_summary (number): Whether to include a summary of the pipeline in the `additional_data` or not
            totals_convert_currency (string): The 3-letter currency code of any of the supported currencies. When supplied, `per_stages_converted` is returned inside `deals_summary` inside `additional_data` which contains the currency-converted total amounts in the given currency per each stage. You may also set this parameter to `default_currency` in which case users default currency is used. Only works when `get_summary` parameter flag is enabled.

        Returns:
            dict[str, Any]: Get deals in a stage

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pipelines/{id}/deals"
        query_params = {k: v for k, v in [('filter_id', filter_id), ('user_id', user_id), ('everyone', everyone), ('stage_id', stage_id), ('start', start), ('limit', limit), ('get_summary', get_summary), ('totals_convert_currency', totals_convert_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_get_movement_statistics(self, id, start_date, end_date, user_id=None) -> dict[str, Any]:
        """
        Retrieves movement statistics for a specific pipeline identified by `{id}`, allowing users to filter the data by `start_date`, `end_date`, and `user_id`.

        Args:
            id (string): id
            start_date (string): The start of the period. Date in format of YYYY-MM-DD.
            end_date (string): The end of the period. Date in format of YYYY-MM-DD.
            user_id (integer): The ID of the user who's pipeline statistics to fetch. If omitted, the authorized user will be used.

        Returns:
            dict[str, Any]: Get pipeline deals conversion rates

        Tags:
            Pipelines
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/pipelines/{id}/movement_statistics"
        query_params = {k: v for k, v in [('start_date', start_date), ('end_date', end_date), ('user_id', user_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_get_all_products(self, user_id=None, filter_id=None, ids=None, first_char=None, get_summary=None, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of products using the "GET" method at the "/products" endpoint, allowing filtering by user ID, filter ID, product IDs, first character, summary preference, and pagination controls via start and limit parameters.

        Args:
            user_id (integer): If supplied, only products owned by the given user will be returned
            filter_id (integer): The ID of the filter to use
            ids (array): An array of integers with the IDs of the products that should be returned in the response
            first_char (string): If supplied, only products whose name starts with the specified letter will be returned (case-insensitive)
            get_summary (boolean): If supplied, the response will return the total numbers of products in the `additional_data.summary.total_count` property
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: List of products

        Tags:
            Products
        """
        url = f"{self.base_url}/products"
        query_params = {k: v for k, v in [('user_id', user_id), ('filter_id', filter_id), ('ids', ids), ('first_char', first_char), ('get_summary', get_summary), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_create_product(self, name, code=None, unit=None, tax=0, active_flag=True, selectable=True, visible_to=None, owner_id=None, prices=None) -> dict[str, Any]:
        """
        Creates a new product resource and returns a success status upon creation.

        Args:
            name (string): The name of the product
            code (string): The product code
            unit (string): The unit in which this product is sold
            tax (number): The tax percentage
            active_flag (boolean): Whether this product will be made active or not
            selectable (boolean): Whether this product can be selected in deals or not
            visible_to (string): The visibility of the product. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            owner_id (integer): The ID of the user who will be marked as the owner of this product. When omitted, the authorized user ID will be used.
            prices (array): An array of objects, each containing: `currency` (string), `price` (number), `cost` (number, optional), `overhead_cost` (number, optional). Note that there can only be one price per product per currency. When `prices` is omitted altogether, a default price of 0 and a default currency based on the company's currency will be assigned.

        Returns:
            dict[str, Any]: Add product data

        Tags:
            Products
        """
        request_body = {
            'name': name,
            'code': code,
            'unit': unit,
            'tax': tax,
            'active_flag': active_flag,
            'selectable': selectable,
            'visible_to': visible_to,
            'owner_id': owner_id,
            'prices': prices,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/products"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_search_by_fields(self, term, fields=None, exact_match=None, include_fields=None, start=None, limit=None) -> Any:
        """
        Retrieves a list of products based on a search term, allowing for customization with parameters such as fields to include, exact match requirements, and pagination options.

        Args:
            term (string): The search term to look for. Minimum 2 characters (or 1 if using `exact_match`). Please note that the search term has to be URL encoded.
            fields (string): A comma-separated string array. The fields to perform the search from. Defaults to all of them. Only the following custom field types are searchable: `address`, `varchar`, `text`, `varchar_auto`, `double`, `monetary` and `phone`. Read more about searching by custom fields <a href=" target="_blank" rel="noopener noreferrer">here</a>.
            exact_match (boolean): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            include_fields (string): Supports including optional fields in the results which are not provided by default
            start (integer): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (integer): Items shown per page

        Returns:
            Any: Success

        Tags:
            Products
        """
        url = f"{self.base_url}/products/search"
        query_params = {k: v for k, v in [('term', term), ('fields', fields), ('exact_match', exact_match), ('include_fields', include_fields), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes the specified product by its ID and returns a success status upon completion.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Deletes a product

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves product details by ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get product information by id

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_update_product_data(self, id, name, code=None, unit=None, tax=0, active_flag=True, selectable=True, visible_to=None, owner_id=None, prices=None) -> dict[str, Any]:
        """
        Updates an entire product at the specified ID using the PUT method, replacing all existing data with new values.

        Args:
            id (string): id
            name (string): The name of the product
            code (string): The product code
            unit (string): The unit in which this product is sold
            tax (number): The tax percentage
            active_flag (boolean): Whether this product will be made active or not
            selectable (boolean): Whether this product can be selected in deals or not
            visible_to (string): The visibility of the product. If omitted, the visibility will be set to the default visibility setting of this item type for the authorized user. Read more about visibility groups <a href="https://support.pipedrive.com/en/article/visibility-groups" target="_blank" rel="noopener noreferrer">here</a>.<h4>Essential / Advanced plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner &amp; followers</td><tr><td>`3`</td><td>Entire company</td></tr></table><h4>Professional / Enterprise plan</h4><table><tr><th style="width: 40px">Value</th><th>Description</th></tr><tr><td>`1`</td><td>Owner only</td><tr><td>`3`</td><td>Owner's visibility group</td></tr><tr><td>`5`</td><td>Owner's visibility group and sub-groups</td></tr><tr><td>`7`</td><td>Entire company</td></tr></table>
            owner_id (integer): The ID of the user who will be marked as the owner of this product. When omitted, the authorized user ID will be used.
            prices (array): An array of objects, each containing: `currency` (string), `price` (number), `cost` (number, optional), `overhead_cost` (number, optional). Note that there can only be one price per product per currency. When `prices` is omitted altogether, a default price of 0 and a default currency based on the company's currency will be assigned.

        Returns:
            dict[str, Any]: Updates product data

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'code': code,
            'unit': unit,
            'tax': tax,
            'active_flag': active_flag,
            'selectable': selectable,
            'visible_to': visible_to,
            'owner_id': owner_id,
            'prices': prices,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/products/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_get_deals(self, id, start=None, limit=None, status=None) -> Any:
        """
        Retrieves a list of deals associated with a specific product, identified by its ID, using the "GET" method at the "/products/{id}/deals" path.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            status (string): Only fetch deals with a specific status. If omitted, all not deleted deals are returned. If set to deleted, deals that have been deleted up to 30 days ago will be included.

        Returns:
            Any: The data of deals that have a product attached

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}/deals"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_list_product_files(self, id, start=None, limit=None, sort=None) -> Any:
        """
        Retrieves a list of files for a specific product by ID, with options to filter using start index, limit results, and sort order.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page
            sort (string): The field name and sorting mode (`field_name_1 ASC` or `field_name_1 DESC`). Supported fields: `update_time`, `id`.

        Returns:
            Any: Success

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}/files"
        query_params = {k: v for k, v in [('start', start), ('limit', limit), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_list_product_followers(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of followers for a specific product identified by `{id}`, allowing optional filtering by pagination parameters `start` and `limit`.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Lists the followers of a product

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}/followers"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_add_follower(self, id, user_id) -> dict[str, Any]:
        """
        Adds a follower to a product using the provided product ID and returns a success status upon addition.

        Args:
            id (string): id
            user_id (integer): The ID of the user

        Returns:
            dict[str, Any]: Adds a follower to a product

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'user_id': user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/products/{id}/followers"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_delete_follower(self, id, follower_id) -> dict[str, Any]:
        """
        Deletes a follower from a product, specified by the product's ID and the follower's ID.

        Args:
            id (string): id
            follower_id (string): follower_id

        Returns:
            dict[str, Any]: Deletes a follower from a product

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if follower_id is None:
            raise ValueError("Missing required parameter 'follower_id'")
        url = f"{self.base_url}/products/{id}/followers/{follower_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def products_list_permitted_users(self, id) -> Any:
        """
        Retrieves a list of permitted users for a specific product identified by its ID using the "GET" method.

        Args:
            id (string): id

        Returns:
            Any: Lists users permitted to access a product

        Tags:
            Products
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/products/{id}/permittedUsers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_delete_multiple_bulk(self, ids) -> dict[str, Any]:
        """
        Deletes product fields by ID using the DELETE method at the "/productFields" path.

        Args:
            ids (string): The comma-separated field IDs to delete

        Returns:
            dict[str, Any]: Mark multiple product fields as deleted

        Tags:
            ProductFields
        """
        url = f"{self.base_url}/productFields"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_get_all_fields(self, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of product fields, supporting optional start and limit parameters for result filtering.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: Get data about all product fields

        Tags:
            ProductFields
        """
        url = f"{self.base_url}/productFields"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_add_new_field(self, name, field_type, options=None) -> dict[str, Any]:
        """
        Adds a new product field using the "POST" method at the "/productFields" endpoint, allowing customization of product data fields for integration purposes.

        Args:
            name (string): The name of the field
            field_type (string): The type of the field<table><tr><th>Value</th><th>Description</th></tr><tr><td>`varchar`</td><td>Text (up to 255 characters)</td><tr><td>`varchar_auto`</td><td>Autocomplete text (up to 255 characters)</td><tr><td>`text`</td><td>Long text (up to 65k characters)</td><tr><td>`double`</td><td>Numeric value</td><tr><td>`monetary`</td><td>Monetary field (has a numeric value and a currency value)</td><tr><td>`date`</td><td>Date (format YYYY-MM-DD)</td><tr><td>`set`</td><td>Options field with a possibility of having multiple chosen options</td><tr><td>`enum`</td><td>Options field with a single possible chosen option</td><tr><td>`user`</td><td>User field (contains a user ID of another Pipedrive user)</td><tr><td>`org`</td><td>Organization field (contains an organization ID which is stored on the same account)</td><tr><td>`people`</td><td>Person field (contains a product ID which is stored on the same account)</td><tr><td>`phone`</td><td>Phone field (up to 255 numbers and/or characters)</td><tr><td>`time`</td><td>Time field (format HH:MM:SS)</td><tr><td>`timerange`</td><td>Time-range field (has a start time and end time value, both HH:MM:SS)</td><tr><td>`daterange`</td><td>Date-range field (has a start date and end date value, both YYYY-MM-DD)</td><tr><td>`address`</td><td>Address field (autocompleted by Google Maps)</dd></table>
            options (array): When `field_type` is either `set` or `enum`, possible options must be supplied as a JSON-encoded sequential array, for example:</br>`[{"label":"red"}, {"label":"blue"}, {"label":"lilac"}]`

        Returns:
            dict[str, Any]: Get the data for a single product field

        Tags:
            ProductFields
        """
        request_body = {
            'name': name,
            'options': options,
            'field_type': field_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/productFields"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes a specific product field by its ID via the Pipedrive API.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete a product field

        Tags:
            ProductFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/productFields/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_get_one_field(self, id) -> dict[str, Any]:
        """
        Retrieves specific product fields by ID using the "GET" method at the "/productFields/{id}" endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get the data for a single product field

        Tags:
            ProductFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/productFields/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def product_fields_update_field(self, id, name=None, options=None) -> dict[str, Any]:
        """
        Updates a product field by replacing its entire record with a new version, specified by the ID provided in the path.

        Args:
            id (string): id
            name (string): The name of the field
            options (array): When `field_type` is either set or enum, possible options on update must be supplied as an array of objects each containing id and label, for example: [{"id":1, "label":"red"},{"id":2, "label":"blue"},{"id":3, "label":"lilac"}]

        Returns:
            dict[str, Any]: Get the data for a single product field

        Tags:
            ProductFields
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'options': options,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/productFields/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_all_projects(self, cursor=None, limit=None, filter_id=None, status=None, phase_id=None, include_archived=None) -> dict[str, Any]:
        """
        Retrieves a list of projects using the "GET" method at the "/projects" endpoint, allowing users to filter results by ID, status, phase, and include archived projects.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, 100 items will be returned. Example: '100'.
            filter_id (integer): The ID of the filter to use
            status (string): If supplied, includes only projects with the specified statuses. Possible values are `open`, `completed`, `canceled` and `deleted`. By default `deleted` projects are not returned. Example: 'open,completed'.
            phase_id (integer): If supplied, only projects in specified phase are returned
            include_archived (boolean): If supplied with `true` then archived projects are also included in the response. By default only not archived projects are returned.

        Returns:
            dict[str, Any]: A list of projects.

        Tags:
            Projects
        """
        url = f"{self.base_url}/projects"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('filter_id', filter_id), ('status', status), ('phase_id', phase_id), ('include_archived', include_archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_create_project(self, title, board_id, phase_id, description=None, status=None, owner_id=None, start_date=None, end_date=None, deal_ids=None, org_id=None, person_id=None, labels=None, template_id=None) -> dict[str, Any]:
        """
        Creates a new GitLab project and returns the created project details.

        Args:
            title (string): The title of the project
            board_id (number): The ID of a project board
            phase_id (number): The ID of a phase on a project board
            description (string): The description of the project
            status (string): The status of the project
            owner_id (number): The ID of a project owner
            start_date (string): The start date of the project. Format: YYYY-MM-DD.
            end_date (string): The end date of the project. Format: YYYY-MM-DD.
            deal_ids (array): An array of IDs of the deals this project is associated with
            org_id (number): The ID of the organization this project is associated with
            person_id (number): The ID of the person this project is associated with
            labels (array): An array of IDs of the labels this project has
            template_id (number): The ID of the template the project will be based on

        Returns:
            dict[str, Any]: Created project.

        Tags:
            Projects
        """
        request_body = {
            'title': title,
            'board_id': board_id,
            'phase_id': phase_id,
            'description': description,
            'status': status,
            'owner_id': owner_id,
            'start_date': start_date,
            'end_date': end_date,
            'deal_ids': deal_ids,
            'org_id': org_id,
            'person_id': person_id,
            'labels': labels,
            'template_id': template_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves a project by its specified ID using the GET method and returns the associated data.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_update_project(self, id, title=None, board_id=None, phase_id=None, description=None, status=None, owner_id=None, start_date=None, end_date=None, deal_ids=None, org_id=None, person_id=None, labels=None) -> dict[str, Any]:
        """
        Updates a project with the specified ID at the path "/projects/{id}" by replacing its entire resource with the provided data using the PUT method.

        Args:
            id (string): id
            title (string): The title of the project
            board_id (number): The ID of the board this project is associated with
            phase_id (number): The ID of the phase this project is associated with
            description (string): The description of the project
            status (string): The status of the project
            owner_id (number): The ID of a project owner
            start_date (string): The start date of the project. Format: YYYY-MM-DD.
            end_date (string): The end date of the project. Format: YYYY-MM-DD.
            deal_ids (array): An array of IDs of the deals this project is associated with
            org_id (number): The ID of the organization this project is associated with
            person_id (number): The ID of the person this project is associated with
            labels (array): An array of IDs of the labels this project has

        Returns:
            dict[str, Any]: Updated project.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'title': title,
            'board_id': board_id,
            'phase_id': phase_id,
            'description': description,
            'status': status,
            'owner_id': owner_id,
            'start_date': start_date,
            'end_date': end_date,
            'deal_ids': deal_ids,
            'org_id': org_id,
            'person_id': person_id,
            'labels': labels,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_mark_as_deleted(self, id) -> dict[str, Any]:
        """
        Deletes a project by its ID using the specified DELETE method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete a project.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_archive_project(self, id) -> dict[str, Any]:
        """
        Archives a project using the provided project ID and returns a status message.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Updated project.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}/archive"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_project_plan(self, id) -> dict[str, Any]:
        """
        Retrieves the plan details for a specific project identified by its unique ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project plan.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}/plan"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_update_project_plan_activity(self, id, activityId, phase_id=None, group_id=None) -> dict[str, Any]:
        """
        Updates a project activity using the PUT method, specifying the project and activity IDs in the path.

        Args:
            id (string): id
            activityId (string): activityId
            phase_id (number): The ID of a phase on a project board
            group_id (number): The ID of a group on a project board

        Returns:
            dict[str, Any]: Updated activity in plan.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if activityId is None:
            raise ValueError("Missing required parameter 'activityId'")
        request_body = {
            'phase_id': phase_id,
            'group_id': group_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{id}/plan/activities/{activityId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_update_plan_task(self, id, taskId, phase_id=None, group_id=None) -> dict[str, Any]:
        """
        Updates a specific task in a project plan and returns the updated task details.

        Args:
            id (string): id
            taskId (string): taskId
            phase_id (number): The ID of a phase on a project board
            group_id (number): The ID of a group on a project board

        Returns:
            dict[str, Any]: Updated task in plan.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        if taskId is None:
            raise ValueError("Missing required parameter 'taskId'")
        request_body = {
            'phase_id': phase_id,
            'group_id': group_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{id}/plan/tasks/{taskId}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_groups(self, id) -> dict[str, Any]:
        """
        Retrieves a list of groups associated with a specific project based on the provided project ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project groups.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}/groups"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_project_tasks(self, id) -> dict[str, Any]:
        """
        Retrieves a list of tasks for a specific project using the project ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A list of tasks.

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}/tasks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_project_activities(self, id) -> dict[str, Any]:
        """
        Retrieves a list of activities for a specific project identified by the path parameter "id" using the "GET" method.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: A list of activities

        Tags:
            Projects
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/{id}/activities"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_all_boards(self) -> dict[str, Any]:
        """
        Retrieves a list of project boards using the GET method.

        Returns:
            dict[str, Any]: A list of project board.

        Tags:
            Projects
        """
        url = f"{self.base_url}/projects/boards"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def project_templates_get_board_details(self, id) -> dict[str, Any]:
        """
        Retrieves a specific project board by its ID using the "GET" method at the "/projects/boards/{id}" endpoint.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project board.

        Tags:
            ProjectTemplates
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/boards/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def projects_get_phases(self, board_id) -> dict[str, Any]:
        """
        Retrieves a list of project phases filtered by board_id.

        Args:
            board_id (integer): ID of the board for which phases are requested Example: '1'.

        Returns:
            dict[str, Any]: A list of project phases.

        Tags:
            Projects
        """
        url = f"{self.base_url}/projects/phases"
        query_params = {k: v for k, v in [('board_id', board_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def project_templates_get_phase_details(self, id) -> dict[str, Any]:
        """
        Retrieves a specific project phase by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project phase.

        Tags:
            ProjectTemplates
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projects/phases/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def project_templates_get_all_templates(self, cursor=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of project templates using the "GET" method at the "/projectTemplates" path, allowing pagination via optional query parameters for cursor and limit.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, up to 500 items will be returned. Example: '500'.

        Returns:
            dict[str, Any]: A list of project template.

        Tags:
            ProjectTemplates
        """
        url = f"{self.base_url}/projectTemplates"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def project_templates_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves the details of a specific project template by its ID.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a project template.

        Tags:
            ProjectTemplates
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/projectTemplates/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def recents_get_changes_after(self, since_timestamp, items=None, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of recent items filtered by timestamp and quantity parameters.

        Args:
            since_timestamp (string): The timestamp in UTC. Format: YYYY-MM-DD HH:MM:SS.
            items (string): Multiple selection of item types to include in the query (optional)
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: List of items changed since "since_timestamp"

        Tags:
            Recents
        """
        url = f"{self.base_url}/recents"
        query_params = {k: v for k, v in [('since_timestamp', since_timestamp), ('items', items), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_get_all_roles(self, start=None, limit=None) -> Any:
        """
        Retrieves a list of roles with optional pagination parameters (start and limit) for managing or displaying role-based data.

        Args:
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: Get all roles

        Tags:
            Roles
        """
        url = f"{self.base_url}/roles"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_create_role(self, name, parent_role_id=None) -> Any:
        """
        Creates a new role using the API by sending a POST request to the "/roles" endpoint.

        Args:
            name (string): The name of the role
            parent_role_id (integer): The ID of the parent role

        Returns:
            Any: Add a role

        Tags:
            Roles
        """
        request_body = {
            'name': name,
            'parent_role_id': parent_role_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/roles"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_mark_as_deleted(self, id) -> Any:
        """
        Deletes a role by its unique identifier and returns a success status upon removal.

        Args:
            id (string): id

        Returns:
            Any: Delete a role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/roles/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_get_one_role(self, id) -> Any:
        """
        Retrieves role details by ID using the GET method from the "/roles/{id}" endpoint.

        Args:
            id (string): id

        Returns:
            Any: Get one role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/roles/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_update_role_details(self, id, parent_role_id=None, name=None) -> Any:
        """
        Updates an existing role identified by the specified ID using the PUT method.

        Args:
            id (string): id
            parent_role_id (integer): The ID of the parent role
            name (string): The name of the role

        Returns:
            Any: Update role details

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'parent_role_id': parent_role_id,
            'name': name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/roles/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_list_role_assignments(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of assignments for a role identified by `{id}`, allowing optional pagination with `start` and `limit` query parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: List assignments for a role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/roles/{id}/assignments"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_assign_user(self, id, user_id) -> Any:
        """
        Assigns roles to specific resources using the "POST" method at the path "/roles/{id}/assignments".

        Args:
            id (string): id
            user_id (integer): The ID of the user

        Returns:
            Any: Add assignment for a role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'user_id': user_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/roles/{id}/assignments"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_get_role_settings(self, id) -> Any:
        """
        Retrieves the settings for a specific role identified by the provided ID.

        Args:
            id (string): id

        Returns:
            Any: List role settings

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/roles/{id}/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_add_or_update_setting(self, id, setting_key, value) -> Any:
        """
        Updates the settings for a specific role identified by the ID and returns a success status.

        Args:
            id (string): id
            setting_key (string): setting_key
            value (integer): Possible values for the `default_visibility` setting depending on the subscription plan:<br> <table class='role-setting'> <caption><b>Essential / Advanced plan</b></caption> <tr><th><b>Value</b></th><th><b>Description</b></th></tr> <tr><td>`1`</td><td>Owner & Followers</td></tr> <tr><td>`3`</td><td>Entire company</td></tr> </table> <br> <table class='role-setting'> <caption><b>Professional / Enterprise plan</b></caption> <tr><th><b>Value</b></th><th><b>Description</b></th></tr> <tr><td>`1`</td><td>Owner only</td></tr> <tr><td>`3`</td><td>Owner&#39;s visibility group</td></tr> <tr><td>`5`</td><td>Owner&#39;s visibility group and sub-groups</td></tr> <tr><td>`7`</td><td>Entire company</td></tr> </table> <br> Read more about visibility groups <a href='https://support.pipedrive.com/en/article/visibility-groups'>here</a>.

        Returns:
            Any: List role settings

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'setting_key': setting_key,
            'value': value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/roles/{id}/settings"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_list_pipeline_visibility(self, id, visible=None) -> Any:
        """
        Retrieves a list of pipelines for a role identified by `{id}` using the `GET` method, allowing optional filtering by visibility.

        Args:
            id (string): id
            visible (boolean): Whether to return the visible or hidden pipelines for the role

        Returns:
            Any: Get either visible or hidden pipeline ids for a role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/roles/{id}/pipelines"
        query_params = {k: v for k, v in [('visible', visible)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_update_pipeline_visibility(self, id, visible_pipeline_ids) -> Any:
        """
        Updates or creates a pipeline for a specific role identified by the "id" parameter using the PUT method.

        Args:
            id (string): id
            visible_pipeline_ids (object): The pipeline IDs to make the pipelines visible (add) and/or hidden (remove) for the specified role. It requires the following JSON structure: `{ "add": "[1]", "remove": "[3, 4]" }`.

        Returns:
            Any: Update pipeline visibility for a role

        Tags:
            Roles
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'visible_pipeline_ids': visible_pipeline_ids,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/roles/{id}/pipelines"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_delete_bulk(self, ids) -> dict[str, Any]:
        """
        Deletes a specified stage in Amazon API Gateway, which removes the stage resource and may impact API usability if it's the only stage associated with a deployment.

        Args:
            ids (string): The comma-separated stage IDs to delete

        Returns:
            dict[str, Any]: Delete multiple stages

        Tags:
            Stages
        """
        url = f"{self.base_url}/stages"
        query_params = {k: v for k, v in [('ids', ids)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_get_all(self, pipeline_id=None, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of stages filtered by pipeline, paginated with start and limit parameters.

        Args:
            pipeline_id (integer): The ID of the pipeline to fetch stages for. If omitted, stages for all pipelines will be fetched.
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: Get all stages

        Tags:
            Stages
        """
        url = f"{self.base_url}/stages"
        query_params = {k: v for k, v in [('pipeline_id', pipeline_id), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_create_new_stage(self, name, pipeline_id, deal_probability=None, rotten_flag=None, rotten_days=None) -> dict[str, Any]:
        """
        Creates a new stage entry via the specified path and returns a success status upon completion.

        Args:
            name (string): The name of the stage
            pipeline_id (integer): The ID of the pipeline to add stage to
            deal_probability (integer): The success probability percentage of the deal. Used/shown when deal weighted values are used.
            rotten_flag (boolean): Whether deals in this stage can become rotten
            rotten_days (integer): The number of days the deals not updated in this stage would become rotten. Applies only if the `rotten_flag` is set.

        Returns:
            dict[str, Any]: Get all stages

        Tags:
            Stages
        """
        request_body = {
            'name': name,
            'pipeline_id': pipeline_id,
            'deal_probability': deal_probability,
            'rotten_flag': rotten_flag,
            'rotten_days': rotten_days,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/stages"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_delete_stage(self, id) -> dict[str, Any]:
        """
        Deletes a stage by its ID using the DELETE method at the "/stages/{id}" path.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Delete stage

        Tags:
            Stages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/stages/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_get_one_stage(self, id, everyone=None) -> dict[str, Any]:
        """
        Retrieves specific stage details by ID, optionally filtering by visibility using the "everyone" query parameter.

        Args:
            id (string): id
            everyone (number): If `everyone=1` is provided, deals summary will return deals owned by every user

        Returns:
            dict[str, Any]: Get stage

        Tags:
            Stages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/stages/{id}"
        query_params = {k: v for k, v in [('everyone', everyone)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_update_details(self, id, name=None, pipeline_id=None, deal_probability=None, rotten_flag=None, rotten_days=None, order_nr=None) -> dict[str, Any]:
        """
        Updates a stage with the specified ID using the "PUT" method at the path "/stages/{id}".

        Args:
            id (string): id
            name (string): The name of the stage
            pipeline_id (integer): The ID of the pipeline to add stage to
            deal_probability (integer): The success probability percentage of the deal. Used/shown when deal weighted values are used.
            rotten_flag (boolean): Whether deals in this stage can become rotten
            rotten_days (integer): The number of days the deals not updated in this stage would become rotten. Applies only if the `rotten_flag` is set.
            order_nr (integer): An order number for this stage. Order numbers should be used to order the stages in the pipeline.

        Returns:
            dict[str, Any]: Get all stages

        Tags:
            Stages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'name': name,
            'pipeline_id': pipeline_id,
            'deal_probability': deal_probability,
            'rotten_flag': rotten_flag,
            'rotten_days': rotten_days,
            'order_nr': order_nr,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/stages/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def stages_get_stage_deals(self, id, filter_id=None, user_id=None, everyone=None, start=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of deals in a specific stage using optional filtering, pagination, and ownership parameters.

        Args:
            id (string): id
            filter_id (integer): If supplied, only deals matching the given filter will be returned
            user_id (integer): If supplied, `filter_id` will not be considered and only deals owned by the given user will be returned. If omitted, deals owned by the authorized user will be returned.
            everyone (number): If supplied, `filter_id` and `user_id` will not be considered – instead, deals owned by everyone will be returned
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            dict[str, Any]: Get deals in a stage

        Tags:
            Stages
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/stages/{id}/deals"
        query_params = {k: v for k, v in [('filter_id', filter_id), ('user_id', user_id), ('everyone', everyone), ('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_get_details(self, id) -> Any:
        """
        Retrieves the subscription details for the specified subscription ID.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/subscriptions/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_delete_marked(self, id) -> Any:
        """
        Deletes a specific subscription using its identifier.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/subscriptions/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_find_by_deal_id(self, dealId) -> Any:
        """
        Retrieves subscription details for a specific deal using the provided deal ID.

        Args:
            dealId (string): dealId

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'")
        url = f"{self.base_url}/subscriptions/find/{dealId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_get_payments(self, id) -> Any:
        """
        Retrieves payment details for a specific subscription identified by its ID.

        Args:
            id (string): id

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/subscriptions/{id}/payments"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_add_recurring(self, deal_id, currency, cadence_type, cycle_amount, start_date, description=None, cycles_count=None, infinite=None, payments=None, update_deal_value=None) -> Any:
        """
        Creates a new recurring subscription using the POST method at the "/subscriptions/recurring" path, allowing for scheduled payments to be set up for ongoing services or products.

        Args:
            deal_id (integer): The ID of the deal this recurring subscription is associated with
            currency (string): The currency of the recurring subscription. Accepts a 3-character currency code.
            cadence_type (string): The interval between payments
            cycle_amount (integer): The amount of each payment
            start_date (string): The start date of the recurring subscription. Format: YYYY-MM-DD
            description (string): The description of the recurring subscription
            cycles_count (integer): Shows how many payments the subscription has. Note that one field must be set: `cycles_count` or `infinite`. If `cycles_count` is set, then `cycle_amount` and `start_date` are also required.
            infinite (boolean): This indicates that the recurring subscription will last until it's manually canceled or deleted. Note that only one field must be set: `cycles_count` or `infinite`.
            payments (array): Array of additional payments. It requires a minimum structure as follows: [{ amount:SUM, description:DESCRIPTION, due_at:PAYMENT_DATE }]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT_DATE with a date (format YYYY-MM-DD).
            update_deal_value (boolean): Indicates that the deal value must be set to recurring subscription's MRR value

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        request_body = {
            'description': description,
            'deal_id': deal_id,
            'currency': currency,
            'cadence_type': cadence_type,
            'cycles_count': cycles_count,
            'cycle_amount': cycle_amount,
            'start_date': start_date,
            'infinite': infinite,
            'payments': payments,
            'update_deal_value': update_deal_value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscriptions/recurring"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_add_installment_subscription(self, deal_id, currency, payments, update_deal_value=None) -> Any:
        """
        Creates an installment subscription with variable payment amounts and dates for a deal, returning details upon successful creation.

        Args:
            deal_id (integer): The ID of the deal this installment subscription is associated with
            currency (string): The currency of the installment subscription. Accepts a 3-character currency code.
            payments (array): Array of payments. It requires a minimum structure as follows: [{ amount:SUM, description:DESCRIPTION, due_at:PAYMENT_DATE }]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT_DATE with a date (format YYYY-MM-DD).
            update_deal_value (boolean): Indicates that the deal value must be set to the installment subscription's total value

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        request_body = {
            'deal_id': deal_id,
            'currency': currency,
            'payments': payments,
            'update_deal_value': update_deal_value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscriptions/installment"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_update_recurring(self, id, effective_date, description=None, cycle_amount=None, payments=None, update_deal_value=None) -> Any:
        """
        Updates a recurring subscription identified by the provided ID using the PUT method.

        Args:
            id (string): id
            effective_date (string): All payments after that date will be affected. Format: YYYY-MM-DD
            description (string): The description of the recurring subscription
            cycle_amount (integer): The amount of each payment
            payments (array): Array of additional payments. It requires a minimum structure as follows: [{ amount:SUM, description:DESCRIPTION, due_at:PAYMENT_DATE }]. Replace SUM with a payment amount, DESCRIPTION with an explanation string, PAYMENT_DATE with a date (format YYYY-MM-DD).
            update_deal_value (boolean): Indicates that the deal value must be set to recurring subscription's MRR value

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'description': description,
            'cycle_amount': cycle_amount,
            'payments': payments,
            'update_deal_value': update_deal_value,
            'effective_date': effective_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscriptions/recurring/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_update_installment_subscription(self, id, payments, update_deal_value=None) -> Any:
        """
        Updates an installment subscription by modifying its details using the provided ID.

        Args:
            id (string): id
            payments (array): Array of payments. It requires a minimum structure as follows: [{ amount:SUM, description:DESCRIPTION, due_at:PAYMENT_DATE }]. Replace SUM with a payment amount, DESCRIPTION with a explanation string, PAYMENT_DATE with a date (format YYYY-MM-DD).
            update_deal_value (boolean): Indicates that the deal value must be set to installment subscription's total value

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'payments': payments,
            'update_deal_value': update_deal_value,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscriptions/installment/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_cancel_recurring_subscription(self, id, end_date=None) -> Any:
        """
        Cancels a recurring subscription by ID using the specified HTTP PUT method and returns a success status upon successful cancellation.

        Args:
            id (string): id
            end_date (string): The subscription termination date. All payments after the specified date will be deleted. The end_date of the subscription will be set to the due date of the payment to follow the specified date. Default value is the current date.

        Returns:
            Any: Success

        Tags:
            Subscriptions
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'end_date': end_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscriptions/recurring/{id}/cancel"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def tasks_list_all_tasks(self, cursor=None, limit=None, assignee_id=None, project_id=None, parent_task_id=None, done=None) -> dict[str, Any]:
        """
        Retrieves a list of tasks with optional filtering by assignee, project, parent task, status, and pagination parameters.

        Args:
            cursor (string): For pagination, the marker (an opaque string value) representing the first item on the next page
            limit (integer): For pagination, the limit of entries to be returned. If not provided, up to 500 items will be returned. Example: '500'.
            assignee_id (integer): If supplied, only tasks that are assigned to this user are returned
            project_id (integer): If supplied, only tasks that are assigned to this project are returned
            parent_task_id (integer): If `null` is supplied then only parent tasks are returned. If integer is supplied then only subtasks of a specific task are returned. By default all tasks are returned.
            done (number): Whether the task is done or not. `0` = Not done, `1` = Done. If not omitted then returns both done and not done tasks.

        Returns:
            dict[str, Any]: A list of tasks.

        Tags:
            Tasks
        """
        url = f"{self.base_url}/tasks"
        query_params = {k: v for k, v in [('cursor', cursor), ('limit', limit), ('assignee_id', assignee_id), ('project_id', project_id), ('parent_task_id', parent_task_id), ('done', done)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tasks_create_task(self, title, project_id, description=None, parent_task_id=None, assignee_id=None, done=None, due_date=None) -> dict[str, Any]:
        """
        Creates a new task entity and returns a success status upon resource creation.

        Args:
            title (string): The title of the task
            project_id (number): The ID of a project
            description (string): The description of the task
            parent_task_id (number): The ID of a parent task. Can not be ID of a task which is already a subtask.
            assignee_id (number): The ID of the user who will be the assignee of the task
            done (string): Whether the task is done or not. 0 = Not done, 1 = Done.
            due_date (string): The due date of the task. Format: YYYY-MM-DD.

        Returns:
            dict[str, Any]: Created task.

        Tags:
            Tasks
        """
        request_body = {
            'title': title,
            'project_id': project_id,
            'description': description,
            'parent_task_id': parent_task_id,
            'assignee_id': assignee_id,
            'done': done,
            'due_date': due_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def tasks_get_details(self, id) -> dict[str, Any]:
        """
        Retrieves a specific task by its unique identifier.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Get a task.

        Tags:
            Tasks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/tasks/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def tasks_update_task(self, id, title=None, project_id=None, description=None, parent_task_id=None, assignee_id=None, done=None, due_date=None) -> dict[str, Any]:
        """
        Updates a specific task by replacing it entirely with new data using the provided task ID.

        Args:
            id (string): id
            title (string): The title of the task
            project_id (number): The ID of the project this task is associated with
            description (string): The description of the task
            parent_task_id (number): The ID of a parent task. Can not be ID of a task which is already a subtask.
            assignee_id (number): The ID of the user who will be the assignee of the task
            done (string): Whether the task is done or not. 0 = Not done, 1 = Done.
            due_date (string): The due date of the task. Format: YYYY-MM-DD.

        Returns:
            dict[str, Any]: Updated task.

        Tags:
            Tasks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'title': title,
            'project_id': project_id,
            'description': description,
            'parent_task_id': parent_task_id,
            'assignee_id': assignee_id,
            'done': done,
            'due_date': due_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def tasks_delete_task(self, id) -> dict[str, Any]:
        """
        Deletes the specified task by its unique identifier and returns a success status upon completion.

        Args:
            id (string): id

        Returns:
            dict[str, Any]: Deleted task.

        Tags:
            Tasks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/tasks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_get_all(self) -> Any:
        """
        Retrieves a list of users using the "GET" method at the "/users" path.

        Returns:
            Any: The list of user objects

        Tags:
            Users, important
        """
        url = f"{self.base_url}/users"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_add_new_user(self, email, access=None, active_flag=True) -> Any:
        """
        Creates a new user account using the POST method and returns a success message upon completion.

        Args:
            email (string): The email of the user
            access (array): The access given to the user. Each item in the array represents access to a specific app. Optionally may include either admin flag or permission set ID to specify which access to give within the app. If both are omitted, the default access for the corresponding app will be used. It requires structure as follows: `[{ app: 'sales', permission_set_id: '62cc4d7f-4038-4352-abf3-a8c1c822b631' }, { app: 'global', admin: true }, { app: 'account_settings' }]`

            active_flag (boolean): Whether the user is active or not. `false` = Not activated, `true` = Activated

        Returns:
            Any: The data of the user

        Tags:
            Users, important
        """
        request_body = {
            'email': email,
            'access': access,
            'active_flag': active_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_find_by_name(self, term, search_by_email=None) -> Any:
        """
        Searches for users by specified criteria or email and returns matching results.

        Args:
            term (string): The search term to look for
            search_by_email (number): When enabled, the term will only be matched against email addresses of users. Default: `false`.

        Returns:
            Any: The list of user objects

        Tags:
            Users, important
        """
        url = f"{self.base_url}/users/find"
        query_params = {k: v for k, v in [('term', term), ('search_by_email', search_by_email)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_get_current_user_data(self) -> Any:
        """
        Retrieves information about the currently authenticated user using the API.

        Returns:
            Any: The data of the logged in user

        Tags:
            Users
        """
        url = f"{self.base_url}/users/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_get_user(self, id) -> Any:
        """
        Retrieves a specific user's details by their unique identifier.

        Args:
            id (string): id

        Returns:
            Any: The data of the user

        Tags:
            Users, important
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/users/{id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_update_details(self, id, active_flag) -> Any:
        """
        Updates a user's information by replacing the entire resource at the specified ID using the PUT method, returning success or error status codes based on the operation's outcome.

        Args:
            id (string): id
            active_flag (boolean): Whether the user is active or not. `false` = Not activated, `true` = Activated

        Returns:
            Any: The data of the user

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            'active_flag': active_flag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/{id}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list_followers(self, id) -> Any:
        """
        Retrieves the list of followers for a specified user.

        Args:
            id (string): id

        Returns:
            Any: The list of user IDs

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/users/{id}/followers"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list_permissions(self, id) -> Any:
        """
        Retrieves the permissions associated with a specific user identified by their unique ID.

        Args:
            id (string): id

        Returns:
            Any: The list of user permissions

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/users/{id}/permissions"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list_role_assignments(self, id, start=None, limit=None) -> Any:
        """
        Retrieves a list of role assignments for a specified user, allowing pagination with optional start and limit query parameters.

        Args:
            id (string): id
            start (integer): Pagination start
            limit (integer): Items shown per page

        Returns:
            Any: List assignments for a role

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/users/{id}/roleAssignments"
        query_params = {k: v for k, v in [('start', start), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list_role_settings(self, id) -> Any:
        """
        Retrieves the role settings for a specific user identified by the `id` path parameter.

        Args:
            id (string): id

        Returns:
            Any: List role settings

        Tags:
            Users
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/users/{id}/roleSettings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_connections_get_all_connections(self) -> Any:
        """
        Retrieves user connections using the "GET" method and returns relevant data.

        Returns:
            Any: The data of user connections

        Tags:
            UserConnections
        """
        url = f"{self.base_url}/userConnections"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_settings_list_authorized_settings(self) -> Any:
        """
        Retrieves user settings metadata including available endpoints for managing user configurations.

        Returns:
            Any: The list of user settings

        Tags:
            UserSettings
        """
        url = f"{self.base_url}/userSettings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_get_all(self) -> Any:
        """
        Retrieves information about existing webhooks, returning details about registered endpoints and event triggers.

        Returns:
            Any: The list of webhooks objects from the logged in company and user

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/webhooks"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_create_new_webhook(self, subscription_url, event_action, event_object, version="1.0", user_id=None, http_auth_user=None, http_auth_password=None) -> Any:
        """
        Sends a webhook notification via the POST method to the "/webhooks" endpoint, triggering event-driven data transfer and processing between systems.

        Args:
            subscription_url (string): A full, valid, publicly accessible URL which determines where to send the notifications. Please note that you cannot use Pipedrive API endpoints as the `subscription_url` and the chosen URL must not redirect to another link.
            event_action (string): The type of action to receive notifications about. Wildcard will match all supported actions.
            event_object (string): The type of object to receive notifications about. Wildcard will match all supported objects.
            version (string): The webhook's version
            user_id (integer): The ID of the user that this webhook will be authorized with. You have the option to use a different user's `user_id`. If it is not set, the current user's `user_id` will be used. As each webhook event is checked against a user's permissions, the webhook will only be sent if the user has access to the specified object(s). If you want to receive notifications for all events, please use a top-level admin user’s `user_id`.
            http_auth_user (string): The HTTP basic auth username of the subscription URL endpoint (if required)
            http_auth_password (string): The HTTP basic auth password of the subscription URL endpoint (if required)

        Returns:
            Any: The created webhook object

        Tags:
            Webhooks
        """
        request_body = {
            'version': version,
            'subscription_url': subscription_url,
            'event_action': event_action,
            'event_object': event_object,
            'user_id': user_id,
            'http_auth_user': http_auth_user,
            'http_auth_password': http_auth_password,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhooks"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhooks_delete_existing_webhook(self, id) -> Any:
        """
        Deletes a webhook endpoint by its ID and returns a confirmation or error message.

        Args:
            id (string): id

        Returns:
            Any: The webhook deletion success response

        Tags:
            Webhooks
        """
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/webhooks/{id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.oauth_request_authorization,
            self.activities_delete_bulk,
            self.activities_list_user_activities,
            self.activities_add_new_activity,
            self.activities_get_all_activities,
            self.activities_mark_as_deleted,
            self.activities_get_details,
            self.activities_update_activity_details,
            self.activity_fields_get_all,
            self.activity_types_mark_as_deleted_bulk,
            self.activity_types_list_all_activity_types,
            self.activity_types_add_new_type,
            self.activity_types_mark_as_deleted,
            self.activity_types_update_type,
            self.billing_get_addons_for_single_company,
            self.call_logs_add_new_log,
            self.call_logs_get_all_logs,
            self.call_logs_delete_log,
            self.call_logs_get_details,
            self.channels_create_new_channel,
            self.channels_delete_channel_by_id,
            self.channels_receive_message,
            self.channels_delete_conversation,
            self.currencies_get_all_supported,
            self.deals_get_all_deals,
            self.deals_create_deal,
            self.deals_delete_bulk,
            self.dealsget_all_deals,
            self.deals_search_by_title_and_notes,
            self.deals_get_summary,
            self.deals_get_timeline_data,
            self.deals_mark_as_deleted,
            self.deals_get_details,
            self.deals_update_properties,
            self.deals_list_activities,
            self.deals_duplicate_deal,
            self.deals_list_deal_files,
            self.deals_list_deal_updates,
            self.deals_list_participants_changelog,
            self.deals_list_followers,
            self.deals_add_follower,
            self.deals_remove_follower,
            self.deals_list_mail_messages,
            self.deals_merge_deals,
            self.deals_list_participants,
            self.deals_add_participant,
            self.deals_delete_participant,
            self.deals_list_permitted_users,
            self.deals_list_persons_associated,
            self.deals_list_deal_products,
            self.deals_add_product_to_deal,
            self.deals_update_product_attachment,
            self.deals_delete_attached_product,
            self.deal_fields_get_all_fields,
            self.deal_fields_add_new_field,
            self.deal_fields_delete_multiple_bulk,
            self.deal_fields_get_one_field,
            self.deal_fields_mark_as_deleted,
            self.deal_fields_update_field,
            self.files_get_all_files,
            self.files_mark_as_deleted,
            self.files_get_one_file,
            self.files_download_file,
            self.filters_delete_bulk,
            self.filters_get_all,
            self.filters_add_new_filter,
            self.filters_get_helpers,
            self.filters_mark_as_deleted,
            self.filters_get_details,
            self.filters_update_filter,
            self.goals_create_report,
            self.goals_get_by_criteria,
            self.goals_update_existing_goal,
            self.goals_mark_as_deleted,
            self.goals_get_result,
            self.item_search_search_multiple_items,
            self.item_search_by_field_values,
            self.leads_get_all,
            self.leads_create_lead,
            self.leads_get_details,
            self.leads_update_lead_properties,
            self.leads_delete_lead,
            self.leads_list_permitted_users,
            self.leads_search_leads,
            self.lead_labels_get_all,
            self.lead_labels_add_new_label,
            self.lead_labels_update_properties,
            self.lead_labels_delete_label,
            self.lead_sources_get_all,
            self.legacy_teams_get_all_teams,
            self.legacy_teams_add_new_team,
            self.legacy_teams_get_data,
            self.legacy_teams_update_team_object,
            self.legacy_teams_get_all_users,
            self.legacy_teams_add_users_to_team,
            self.legacy_teams_get_user_teams,
            self.mailbox_get_mail_message,
            self.mailbox_get_mail_threads,
            self.mailbox_mark_thread_deleted,
            self.mailbox_get_mail_thread,
            self.mailbox_get_all_mail_messages,
            self.meetings_link_user_provider,
            self.meetings_remove_user_provider_link,
            self.notes_get_all,
            self.notes_create_note,
            self.notes_delete_note,
            self.notes_get_details,
            self.notes_update_note,
            self.notes_get_all_comments,
            self.notes_add_new_comment,
            self.notes_get_comment_details,
            self.notes_update_comment,
            self.notes_delete_comment,
            self.note_fields_get_all_note_fields,
            self.organizations_delete_multiple_bulk,
            self.organizations_get_all,
            self.organizations_add_new_organization,
            self.organizations_list_all_organizations,
            self.organizations_search_by_criteria,
            self.organizations_delete_marked_organization,
            self.organizations_get_details,
            self.organizations_update_properties,
            self.organizations_list_activities,
            self.organizations_list_deals,
            self.organizations_list_attached_files,
            self.organizations_list_updates_about,
            self.organizations_list_followers,
            self.organizations_add_follower,
            self.organizations_delete_follower,
            self.organizations_list_mail_messages,
            self.organizations_merge_two,
            self.organizations_list_permitted_users,
            self.organizations_list_persons,
            self.organization_fields_get_all_fields,
            self.organization_fields_add_new_field,
            self.organization_fields_delete_multiple_bulk,
            self.organization_fields_get_specific_field,
            self.organization_fields_mark_as_deleted,
            self.organization_fields_update_field,
            self.organization_relationships_get_all_relationships,
            self.organization_relationships_create_new_relationship,
            self.organization_relationships_delete_by_id,
            self.organization_relationships_get_by_id,
            self.organization_relationships_update_and_return,
            self.permission_sets_get_all,
            self.permission_sets_get_one,
            self.permission_sets_list_assignments,
            self.persons_delete_multiple_bulk,
            self.persons_list_all_persons,
            self.persons_create_new_person,
            self.persons_get_all,
            self.persons_search_by_criteria,
            self.persons_mark_as_deleted,
            self.persons_get_person_details,
            self.persons_update_properties,
            self.persons_list_activities,
            self.persons_list_deals,
            self.persons_list_person_files,
            self.persons_list_updates_about,
            self.persons_list_followers,
            self.persons_add_follower,
            self.persons_delete_follower,
            self.persons_list_mail_messages,
            self.persons_merge_two,
            self.persons_list_permitted_users,
            self.persons_list_products,
            self.person_fields_get_all_fields,
            self.person_fields_add_new_field,
            self.person_fields_delete_multiple_bulk,
            self.person_fields_get_specific_field,
            self.person_fields_mark_as_deleted,
            self.person_fields_update_field,
            self.pipelines_get_all,
            self.pipelines_create_new_pipeline,
            self.pipelines_delete_pipeline,
            self.pipelines_get_one_pipeline_summary,
            self.pipelines_update_properties,
            self.pipelines_get_conversion_statistics,
            self.pipelines_list_deals,
            self.pipelines_get_movement_statistics,
            self.products_get_all_products,
            self.products_create_product,
            self.products_search_by_fields,
            self.products_mark_as_deleted,
            self.products_get_details,
            self.products_update_product_data,
            self.products_get_deals,
            self.products_list_product_files,
            self.products_list_product_followers,
            self.products_add_follower,
            self.products_delete_follower,
            self.products_list_permitted_users,
            self.product_fields_delete_multiple_bulk,
            self.product_fields_get_all_fields,
            self.product_fields_add_new_field,
            self.product_fields_mark_as_deleted,
            self.product_fields_get_one_field,
            self.product_fields_update_field,
            self.projects_get_all_projects,
            self.projects_create_project,
            self.projects_get_details,
            self.projects_update_project,
            self.projects_mark_as_deleted,
            self.projects_archive_project,
            self.projects_get_project_plan,
            self.projects_update_project_plan_activity,
            self.projects_update_plan_task,
            self.projects_get_groups,
            self.projects_get_project_tasks,
            self.projects_get_project_activities,
            self.projects_get_all_boards,
            self.project_templates_get_board_details,
            self.projects_get_phases,
            self.project_templates_get_phase_details,
            self.project_templates_get_all_templates,
            self.project_templates_get_details,
            self.recents_get_changes_after,
            self.roles_get_all_roles,
            self.roles_create_role,
            self.roles_mark_as_deleted,
            self.roles_get_one_role,
            self.roles_update_role_details,
            self.roles_list_role_assignments,
            self.roles_assign_user,
            self.roles_get_role_settings,
            self.roles_add_or_update_setting,
            self.roles_list_pipeline_visibility,
            self.roles_update_pipeline_visibility,
            self.stages_delete_bulk,
            self.stages_get_all,
            self.stages_create_new_stage,
            self.stages_delete_stage,
            self.stages_get_one_stage,
            self.stages_update_details,
            self.stages_get_stage_deals,
            self.subscriptions_get_details,
            self.subscriptions_delete_marked,
            self.subscriptions_find_by_deal_id,
            self.subscriptions_get_payments,
            self.subscriptions_add_recurring,
            self.subscriptions_add_installment_subscription,
            self.subscriptions_update_recurring,
            self.subscriptions_update_installment_subscription,
            self.subscriptions_cancel_recurring_subscription,
            self.tasks_list_all_tasks,
            self.tasks_create_task,
            self.tasks_get_details,
            self.tasks_update_task,
            self.tasks_delete_task,
            self.users_get_all,
            self.users_add_new_user,
            self.users_find_by_name,
            self.users_get_current_user_data,
            self.users_get_user,
            self.users_update_details,
            self.users_list_followers,
            self.users_list_permissions,
            self.users_list_role_assignments,
            self.users_list_role_settings,
            self.user_connections_get_all_connections,
            self.user_settings_list_authorized_settings,
            self.webhooks_get_all,
            self.webhooks_create_new_webhook,
            self.webhooks_delete_existing_webhook
        ]
