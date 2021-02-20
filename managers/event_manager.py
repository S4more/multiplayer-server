from typing import Type, Union
from events.mouse import Mouse
from events.vote import Vote
from events.Events import Event
class EventManager:
    # The events inside this list are the essential events,
    # these who you will not add on demand. 
    events = [
        Mouse,
        Vote
    ]

    def __init__(self):
        # Create an instance of each one of the events
        self.events = list(map(lambda func: func(), self.events))

    def getEventByClassName(self, name: str) -> Union[Event, None]:
        '''Gets an event based on the class name of the event and
        returns the event itself if it exists.'''
        for event in self.events:
            if name == event.__class__.__name__:
                return event
        return None

    def add_event(self, event: Type[Event]):
        '''Add an event based on a class to the EventManager
        and returns the instance.'''
        self.events.append(event())
        return self.events[-1]

    def rm_event(self, event):
        '''Remove an event based on a instace from the EventManager'''
        self.events.remove(event)

    async def forward_event(self, data, player, users):
        '''Forward the websocket data to its respective event.'''
        # Inject all the users in data.
        data['users'] = users
        for event in self.events:
            if (data["action"] == event.type):
                event.handle(player, data['value'])
                await event.notify(users) # it doesn't make any sense
                return
        print(f" Action {data['action']} is not registered.")
