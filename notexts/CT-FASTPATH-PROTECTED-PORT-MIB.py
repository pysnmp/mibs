#
# PySNMP MIB module CT-FASTPATH-PROTECTED-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:54:23 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ctFastPathProtectedPortMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastPathProtectedPortMib")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, iso, Bits, Counter64, MibIdentifier, Integer32, Gauge32, IpAddress, NotificationType, Unsigned32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "iso", "Bits", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "NotificationType", "Unsigned32", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFastPathProtectedPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1))
ctFastPathProtectedPortMIB.setRevisions(('2006-03-06 15:01',))
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setLastUpdated('200603061501Z')
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setOrganization('Enterasys Networks, Inc.')
ctAgentSwitchConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1))
ctAgentSwitchProtectedPortConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18))
ctAgentSwitchProtectedPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1), )
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortTable.setStatus('current')
ctAgentSwitchProtectedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1), ).setIndexNames((0, "CT-FASTPATH-PROTECTED-PORT-MIB", "ctAgentSwitchProtectedPortGroupId"))
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortEntry.setStatus('current')
ctAgentSwitchProtectedPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupId.setStatus('current')
ctAgentSwitchProtectedPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupName.setStatus('current')
ctAgentSwitchProtectedPortPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortPortList.setStatus('current')
mibBuilder.exportSymbols("CT-FASTPATH-PROTECTED-PORT-MIB", ctAgentSwitchConfigGroup=ctAgentSwitchConfigGroup, ctAgentSwitchProtectedPortTable=ctAgentSwitchProtectedPortTable, ctAgentSwitchProtectedPortGroupId=ctAgentSwitchProtectedPortGroupId, ctAgentSwitchProtectedPortGroupName=ctAgentSwitchProtectedPortGroupName, ctFastPathProtectedPortMIB=ctFastPathProtectedPortMIB, PYSNMP_MODULE_ID=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortConfigGroup=ctAgentSwitchProtectedPortConfigGroup, ctAgentSwitchProtectedPortPortList=ctAgentSwitchProtectedPortPortList, ctAgentSwitchProtectedPortEntry=ctAgentSwitchProtectedPortEntry)
