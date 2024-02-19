#
# PySNMP MIB module CT-FASTPATH-PROTECTED-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.1.10 at Mon Feb 19 02:56:42 2024
# On host fv-az1016-227 platform Linux version 6.2.0-1019-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ctFastPathProtectedPortMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastPathProtectedPortMib")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, Bits, ModuleIdentity, iso, TimeTicks, Counter32, Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Bits", "ModuleIdentity", "iso", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("CT-FASTPATH-PROTECTED-PORT-MIB", ctAgentSwitchProtectedPortPortList=ctAgentSwitchProtectedPortPortList, ctFastPathProtectedPortMIB=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortConfigGroup=ctAgentSwitchProtectedPortConfigGroup, ctAgentSwitchProtectedPortEntry=ctAgentSwitchProtectedPortEntry, ctAgentSwitchProtectedPortTable=ctAgentSwitchProtectedPortTable, ctAgentSwitchProtectedPortGroupId=ctAgentSwitchProtectedPortGroupId, PYSNMP_MODULE_ID=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortGroupName=ctAgentSwitchProtectedPortGroupName, ctAgentSwitchConfigGroup=ctAgentSwitchConfigGroup)
