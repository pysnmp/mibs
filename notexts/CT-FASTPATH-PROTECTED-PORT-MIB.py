#
# PySNMP MIB module CT-FASTPATH-PROTECTED-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:09:45 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ctFastPathProtectedPortMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastPathProtectedPortMib")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, iso, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "iso", "TimeTicks", "Integer32", "NotificationType")
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
mibBuilder.exportSymbols("CT-FASTPATH-PROTECTED-PORT-MIB", ctAgentSwitchProtectedPortConfigGroup=ctAgentSwitchProtectedPortConfigGroup, PYSNMP_MODULE_ID=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortGroupId=ctAgentSwitchProtectedPortGroupId, ctAgentSwitchProtectedPortPortList=ctAgentSwitchProtectedPortPortList, ctFastPathProtectedPortMIB=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortTable=ctAgentSwitchProtectedPortTable, ctAgentSwitchProtectedPortEntry=ctAgentSwitchProtectedPortEntry, ctAgentSwitchProtectedPortGroupName=ctAgentSwitchProtectedPortGroupName, ctAgentSwitchConfigGroup=ctAgentSwitchConfigGroup)
