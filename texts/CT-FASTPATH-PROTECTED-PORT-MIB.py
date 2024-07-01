#
# PySNMP MIB module CT-FASTPATH-PROTECTED-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:19:23 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ctFastPathProtectedPortMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastPathProtectedPortMib")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, iso, Counter64, TimeTicks, ModuleIdentity, NotificationType, Unsigned32, Bits, Gauge32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "iso", "Counter64", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFastPathProtectedPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1))
ctFastPathProtectedPortMIB.setRevisions(('2006-03-06 15:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setLastUpdated('200603061501Z')
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setContactInfo('Postal:  Enterasys Networks\n                  50 Minuteman Rd.\n                  Andover, MA 01810-1008\n                  USA\n         Phone:   +1 978 684 1000\n         E-mail:  support@enterasys.com\n         WWW:     http://www.enterasys.com')
if mibBuilder.loadTexts: ctFastPathProtectedPortMIB.setDescription('The Enterasys MIB for FASTPATH Protected Port.')
ctAgentSwitchConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1))
ctAgentSwitchProtectedPortConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18))
ctAgentSwitchProtectedPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1), )
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortTable.setStatus('current')
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortTable.setDescription("The switch's protected port mapping table")
ctAgentSwitchProtectedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1), ).setIndexNames((0, "CT-FASTPATH-PROTECTED-PORT-MIB", "ctAgentSwitchProtectedPortGroupId"))
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortEntry.setStatus('current')
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortEntry.setDescription('Protected ports assigned to groups.')
ctAgentSwitchProtectedPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupId.setStatus('current')
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupId.setDescription('The group that this port belongs to')
ctAgentSwitchProtectedPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupName.setStatus('current')
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortGroupName.setDescription('The name of the group')
ctAgentSwitchProtectedPortPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortPortList.setStatus('current')
if mibBuilder.loadTexts: ctAgentSwitchProtectedPortPortList.setDescription('The set of ports that are protected in this group')
mibBuilder.exportSymbols("CT-FASTPATH-PROTECTED-PORT-MIB", ctAgentSwitchProtectedPortConfigGroup=ctAgentSwitchProtectedPortConfigGroup, PYSNMP_MODULE_ID=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortGroupName=ctAgentSwitchProtectedPortGroupName, ctFastPathProtectedPortMIB=ctFastPathProtectedPortMIB, ctAgentSwitchConfigGroup=ctAgentSwitchConfigGroup, ctAgentSwitchProtectedPortPortList=ctAgentSwitchProtectedPortPortList, ctAgentSwitchProtectedPortGroupId=ctAgentSwitchProtectedPortGroupId, ctAgentSwitchProtectedPortTable=ctAgentSwitchProtectedPortTable, ctAgentSwitchProtectedPortEntry=ctAgentSwitchProtectedPortEntry)
