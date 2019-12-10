from enum import Enum

class ChoiceEnum(Enum):
    # Get value and name as list of tuple
    @classmethod
    def choices(cls):
        choices = list()

        # Loop defined enums
        for item in cls:
            choices.append((str(item.value), item.name))

        # return in tuple
        return tuple(choices)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value
    
    # get value as list
    @classmethod
    def value_list(cls):
        value_list = list()
         
        # Loop defined enaum
        for item in cls:
            value_list.append(item.value)
        return value_list
    
    def __int__(self):
        return self.value
        
    @classmethod
    def dict_list(cls):
        dict_list = list()
        
        for item in cls:
            dict_list.append({'type': str(item.name), 'value': str(item.value)})
        
        return dict_list

    @classmethod
    def discard_dict_list(cls, discard=[]):
        dict_list = list()
        
        for item in cls:
            if not item.name in discard:
                dict_list.append({'type': str(item.name), 'value': str(item.value)})
        return dict_list

    @classmethod
    def keep_only_dict_list(cls, keep=[]):
        dict_list = list()
        
        for item in cls:
            if item.name in keep:
                dict_list.append({'type': str(item.name), 'value': str(item.value)})
        return dict_list

    

    
    
class UserType(ChoiceEnum):
    ADMIN = 1
    EXAMINEE = 2