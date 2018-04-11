""" Cisco_IOS_XR_sysadmin_entity_state_mib 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ENTITYSTATEMIB(Entity):
    """
    
    
    .. attribute:: entstatetable
    
    	
    	**type**\:  :py:class:`Entstatetable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_mib.ENTITYSTATEMIB.Entstatetable>`
    
    

    """

    _prefix = 'ENTITY_STATE_MIB'
    _revision = '2017-04-12'

    def __init__(self):
        super(ENTITYSTATEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-STATE-MIB"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-entity-state-mib"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("entStateTable", ("entstatetable", ENTITYSTATEMIB.Entstatetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.entstatetable = ENTITYSTATEMIB.Entstatetable()
        self.entstatetable.parent = self
        self._children_name_map["entstatetable"] = "entStateTable"
        self._children_yang_names.add("entStateTable")
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-entity-state-mib:ENTITY-STATE-MIB"


    class Entstatetable(Entity):
        """
        
        
        .. attribute:: entstateentry
        
        	
        	**type**\: list of  		 :py:class:`Entstateentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_mib.ENTITYSTATEMIB.Entstatetable.Entstateentry>`
        
        

        """

        _prefix = 'ENTITY_STATE_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYSTATEMIB.Entstatetable, self).__init__()

            self.yang_name = "entStateTable"
            self.yang_parent_name = "ENTITY-STATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entStateEntry", ("entstateentry", ENTITYSTATEMIB.Entstatetable.Entstateentry))])
            self._leafs = OrderedDict()

            self.entstateentry = YList(self)
            self._segment_path = lambda: "entStateTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-state-mib:ENTITY-STATE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYSTATEMIB.Entstatetable, [], name, value)


        class Entstateentry(Entity):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entstatelastchanged
            
            	
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: entstateadmin
            
            	
            	**type**\:  :py:class:`EntityAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib.EntityAdminState>`
            
            .. attribute:: entstateoper
            
            	
            	**type**\:  :py:class:`EntityOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib.EntityOperState>`
            
            .. attribute:: entstateusage
            
            	
            	**type**\:  :py:class:`EntityUsageState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib.EntityUsageState>`
            
            .. attribute:: entstatealarm
            
            	
            	**type**\:  :py:class:`EntityAlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib.EntityAlarmStatus>`
            
            .. attribute:: entstatestandby
            
            	
            	**type**\:  :py:class:`EntityStandbyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib.EntityStandbyStatus>`
            
            

            """

            _prefix = 'ENTITY_STATE_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYSTATEMIB.Entstatetable.Entstateentry, self).__init__()

                self.yang_name = "entStateEntry"
                self.yang_parent_name = "entStateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.int32, 'entPhysicalIndex')),
                    ('entstatelastchanged', YLeaf(YType.str, 'entStateLastChanged')),
                    ('entstateadmin', YLeaf(YType.enumeration, 'entStateAdmin')),
                    ('entstateoper', YLeaf(YType.enumeration, 'entStateOper')),
                    ('entstateusage', YLeaf(YType.enumeration, 'entStateUsage')),
                    ('entstatealarm', YLeaf(YType.bits, 'entStateAlarm')),
                    ('entstatestandby', YLeaf(YType.enumeration, 'entStateStandby')),
                ])
                self.entphysicalindex = None
                self.entstatelastchanged = None
                self.entstateadmin = None
                self.entstateoper = None
                self.entstateusage = None
                self.entstatealarm = Bits()
                self.entstatestandby = None
                self._segment_path = lambda: "entStateEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-state-mib:ENTITY-STATE-MIB/entStateTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYSTATEMIB.Entstatetable.Entstateentry, ['entphysicalindex', 'entstatelastchanged', 'entstateadmin', 'entstateoper', 'entstateusage', 'entstatealarm', 'entstatestandby'], name, value)

    def clone_ptr(self):
        self._top_entity = ENTITYSTATEMIB()
        return self._top_entity
