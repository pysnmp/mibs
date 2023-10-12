#
# PySNMP MIB module CTRON-SMARTTRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SMARTTRUNK-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 08:54:45 2023
# On host fv-az792-520 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ctSmartTrunkBranch, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctSmartTrunkBranch")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, Bits, NotificationType, ObjectIdentity, IpAddress, iso, MibIdentifier, Counter64, TimeTicks, Integer32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "NotificationType", "ObjectIdentity", "IpAddress", "iso", "MibIdentifier", "Counter64", "TimeTicks", "Integer32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
ctSmartTrunk = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1))
if mibBuilder.loadTexts: ctSmartTrunk.setLastUpdated('199812160000Z')
if mibBuilder.loadTexts: ctSmartTrunk.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ctSmartTrunk.setContactInfo('Cabletron Systems, Inc.\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@cabletron.com\n     http://www.ctron.com')
if mibBuilder.loadTexts: ctSmartTrunk.setDescription('This mib module defines a portion of the SNMP enterprise MIBs under Cabletron\n             enterprise OID pertaining to configuration of Smart TRUNK network links.')
ctSmartTrunkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1))
ctSmartTrunkDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2))
class CTSmartTrunkProtocol(TextualConvention, Integer32):
    description = 'Type of trunking protocol used. LLAP based switches should use decHuntGroup.\n            noProcol applies to all other types of connections.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noProtocol", 1), ("decHuntGroup", 2))

class CTSmartTrunkIndex(TextualConvention, Integer32):
    description = "Most of the tables in this MIB are indexed in whole\n                 or in part by 'ctTrunkIndex' - not by 'ifIndex'.\n                 Why is there a separate index?\n                 Traditionally, ifIndex values are chosen by agents,\n                 and are permitted to change across restarts.  Using\n                 ifIndex to index ctTrunkConfigTable could complicate\n                 row creation and/or cause interoperability problems\n                 (if each agent had special restrictions on ifIndex).\n                 Having a separate index avoids these problems."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CTSmartTrunkName(DisplayString):
    description = 'A textual description of this virtual port.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class CTSmartTrunkLoadBalanceType(TextualConvention, Integer32):
    description = 'The algorithm in use to assign flows to each link in a Smart TRUNK.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("balancingUnspecified", 1), ("roundRobin", 2), ("linkUtilization", 3))

ctTrunkGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTrunkGlobalStatus.setStatus('current')
if mibBuilder.loadTexts: ctTrunkGlobalStatus.setDescription('The state of Smart TRUNK capability for this entire managed entity. Default Value is True(1). If set to False(2)\n                 all smart trunks are put into ifAdminStatus down.')
ctTrunkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3), )
if mibBuilder.loadTexts: ctTrunkConfigTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigTable.setDescription("A table describing all of the trunk interfaces\n                   implemented by this host.  Each trunk has a row\n                   in the MIB-II/RFC 2233 Interfaces table (describing\n                   the structure of the trunk interface it presents to higher\n                   layers).  Each trunk interface also has a row in this and\n                   other CTRON-SMARTTRUNK-MIB tables. Smart Trunks use\n                   ifType propMultiplexor(54). Counters represent the aggregate of\n                   all physcal links.\n\n                   Unlike hardware ports, trunk interfaces can be created by\n                   management.  However, the RFC 2233 Interfaces table\n                   does not directly support row creation.  Therefore,\n                   creating or deleting a row in the ctTrunkConfigTable is\n                   defined to have the side effect of creating or\n                   deleting corresponding rows in\n\n                       -  the MIB-II / RFC 2233 Interfaces table,\n                       -  any other dependent tables\n\n                   New Interfaces table rows for trunk intefaces\n                   always have 'ifAdminStatus' set to 'down' until the row\n                   state is becomes Active. Then administration of the\n                   interface uses normal ifTable ifAdminStatus to enabled it.")
ctTrunkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"))
if mibBuilder.loadTexts: ctTrunkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigEntry.setDescription('Each table entry contains configuration information for one trunk interface.')
ctTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 1), CTSmartTrunkIndex())
if mibBuilder.loadTexts: ctTrunkIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkIndex.setDescription('A value which uniquely identifies this conceptual\n                   row in the ctTrunkConfigTable. The Table allows sparse values.\n\n                   If the conceptual row identified by this value of\n                   ctTrunkIndex is recreated following an agent restart,\n                   the same value of ctTrunkIndex must be used to identify\n                   the recreated row.  (However, the Interfaces table\n                   index associated with the client may change. ifAlias in ifXTable is used\n                   then to reassociate ifIndexes based on ifAlias. In the case of the SSR,\n                   Smart Trunks are manipulated as st.ctTrunkIndex')
ctTrunkConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 2), CTSmartTrunkName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigName.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigName.setDescription("The Trunk's Name, just for informational purposes. It may be changed\n                   regardless of the RowStatus value.")
ctTrunkConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 3), CTSmartTrunkProtocol().clone('decHuntGroup')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigProtocol.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigProtocol.setDescription('Trunking protocol in use. Once the row is active, it can not be changed.')
ctTrunkConfigLoadBalance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 4), CTSmartTrunkLoadBalanceType().clone('balancingUnspecified')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigLoadBalance.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigLoadBalance.setDescription('The type of load balance algorithm applied to this trunk.\n                   Once Row is active, the agent may override this value with an implmentation specific\n                   default.')
ctTrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkIfIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkIfIndex.setDescription('The ifIndex in ifTable, ifXTable that is associated with the trunk that is\n                 represented by this row.')
ctTrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkRowStatus.setStatus('current')
if mibBuilder.loadTexts: ctTrunkRowStatus.setDescription("This object lets network managers create and delete\n                   trunk interfaces, on systems that support this\n                   optional capability.\n\n                   It does not control the activation and deactivation\n                   of these interfaces; they are controlled by 'ifAdminStatus'\n                   in the ifTable.  However, changing row state from active\n                   to notInService. will have the side effect of changing\n                   their 'ifAdminStatus' values to 'noPresent' or 'down',\n                   thus causing any active trunk connections to be terminated.\n\n                   When creating a trunk interface, it is up to the\n                   management station to determine a suitable 'ctTrunkIndex'.\n                   To facilitate interoperability, agents should not put\n                   any restrictions on the 'ctTrunkIndex' beyond the obvious\n                   ones that it be valid and unused.\n\n                   The Managed Objects that must be set in this table\n                   for a row to change from nonExistent/notReady to notInService/Active\n                   is simply an index. Ports can then be added to the Smart TRUNK\n                   via the ifStackTable.\n\n                   If you create a trunk interface via this object,\n                   it will initially have\n                       'ifAdminStatus' = 'down'\n                       'ifOperStatus' = 'down' when RowStatus is changed to active.")
ctTrunkConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4), )
if mibBuilder.loadTexts: ctTrunkConnectionTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConnectionTable.setDescription('This table describes how local interfaces that are\n                   participating in a trunk are connected to remote\n                   interfaces.\n\n                   With this table, a management entity can determine\n                   that (for example) local interfaces 3, 4, and 6 are\n                   connected to remote interfaces 10, 17, and 19.\n\n                   This table is useful to debug configuration errors\n                   with remote devices. If ifAdminStatus/ifOperState is\n                   up, and no corresponding row is found in this table,\n                   then a management station can assume a the remote\n                   end does not have the decHuntGroup protocol active.\n\n                   Note:  this entire table is read-only.  Rows are\n                   created and deleted from this table as a side\n                   effect of trunks being created and deleted.\n\n                   Note:  a managment entity could determine (for\n                   example) that interface 3 was participating in\n                   trunk 3 by using the ifStackTable and ctTrunkIfIndex.')
ctTrunkConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConnectionEntry.setDescription('Each table entry contains configuration information\n                   for one interface that is participating in a trunk.')
ctTrunkPortRemoteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkPortRemoteIfIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkPortRemoteIfIndex.setDescription('The ifIndex of the interface at the other end of\n                  this part of the trunk link.  If this value is 0,\n                  then for some reason there is no interface on the\n                  other side of this link.  This might be a temporary\n                  condition or it might represent a real problem.\n\n                  Note:  this table is indexed by ifIndex.  So the\n                  index is the local ifIndex value and\n                  ctTrunkPortRemoteIfIndex is the remote ifIndex.')
ctTrunkLLAPRequirement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("notRequired", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkLLAPRequirement.setStatus('current')
if mibBuilder.loadTexts: ctTrunkLLAPRequirement.setDescription('Indicates whether this managed entity requires the\n                 LLAP updates to perform the trunking function.\n\n                 Certain families of products require LLAP (decHuntGroup Protocol)\n                 order for the Smart TRUNK functionality to work.\n                 A value of 1 implies that LLAP is necessary for smart-trunking\n                 to work on this platform, a value of 2 indicates that it is\n                 not necessary.')
ctTrunkMaxTrunks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkMaxTrunks.setStatus('current')
if mibBuilder.loadTexts: ctTrunkMaxTrunks.setDescription('The maximum number of trunks that can be configured\n                on this managed entity.')
ctTrunkFlowDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4), )
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticTable.setDescription('Provide a means to programmatically evaluate the load\n         balancing of a smart trunk. Assumes that load balancing is done on a\n         flow by flow basis.')
ctTrunkFlowDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticEntry.setDescription('Each row refers to a specific smart trunk and port within\n         that smart trunk.')
ctTrunkFlowDiagnosticInstalledFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticInstalledFlows.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticInstalledFlows.setDescription('A counter of the flows installed on this port since it was\n         first operational.')
ctTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3))
ctTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1))
ctTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2))
ctTrunkComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkConfGroupV10"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkComplianceV10 = ctTrunkComplianceV10.setStatus('current')
if mibBuilder.loadTexts: ctTrunkComplianceV10.setDescription('The compliance statement for the CTRON-SMARTTRUNK-MIB.')
ctTrunkConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkGlobalStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkRowStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigName"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigProtocol"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigLoadBalance"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkPortRemoteIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkLLAPRequirement"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkMaxTrunks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkConfGroupV10 = ctTrunkConfGroupV10.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the CTRON-SMARTTRUNK-MIB.')
ctTrunkFlowDiagnosticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 2)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticInstalledFlows"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkFlowDiagnosticGroup = ctTrunkFlowDiagnosticGroup.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticGroup.setDescription("A collection of diagnostic information related to\n                interfaces participating in SmartTrunks; specifically\n                to interfaces on devices that use 'flows'.")
mibBuilder.exportSymbols("CTRON-SMARTTRUNK-MIB", CTSmartTrunkProtocol=CTSmartTrunkProtocol, ctTrunkConfigTable=ctTrunkConfigTable, ctTrunkIfIndex=ctTrunkIfIndex, ctTrunkFlowDiagnosticInstalledFlows=ctTrunkFlowDiagnosticInstalledFlows, CTSmartTrunkIndex=CTSmartTrunkIndex, ctTrunkFlowDiagnosticTable=ctTrunkFlowDiagnosticTable, ctTrunkComplianceV10=ctTrunkComplianceV10, ctTrunkLLAPRequirement=ctTrunkLLAPRequirement, ctTrunkConfGroupV10=ctTrunkConfGroupV10, ctTrunkConfigName=ctTrunkConfigName, ctSmartTrunkConfig=ctSmartTrunkConfig, ctTrunkGroups=ctTrunkGroups, ctSmartTrunkDebug=ctSmartTrunkDebug, ctTrunkConnectionTable=ctTrunkConnectionTable, ctTrunkFlowDiagnosticEntry=ctTrunkFlowDiagnosticEntry, ctTrunkConfigEntry=ctTrunkConfigEntry, ctTrunkPortRemoteIfIndex=ctTrunkPortRemoteIfIndex, ctSmartTrunk=ctSmartTrunk, ctTrunkCompliances=ctTrunkCompliances, ctTrunkConfigLoadBalance=ctTrunkConfigLoadBalance, ctTrunkRowStatus=ctTrunkRowStatus, ctTrunkFlowDiagnosticGroup=ctTrunkFlowDiagnosticGroup, CTSmartTrunkLoadBalanceType=CTSmartTrunkLoadBalanceType, ctTrunkIndex=ctTrunkIndex, CTSmartTrunkName=CTSmartTrunkName, ctTrunkGlobalStatus=ctTrunkGlobalStatus, ctTrunkConnectionEntry=ctTrunkConnectionEntry, ctTrunkConformance=ctTrunkConformance, PYSNMP_MODULE_ID=ctSmartTrunk, ctTrunkMaxTrunks=ctTrunkMaxTrunks, ctTrunkConfigProtocol=ctTrunkConfigProtocol)
