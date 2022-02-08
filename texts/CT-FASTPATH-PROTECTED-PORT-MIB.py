#
# PySNMP MIB module CT-FASTPATH-PROTECTED-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:15:34 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ctFastPathProtectedPortMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastPathProtectedPortMib")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, NotificationType, ModuleIdentity, TimeTicks, Counter64, Counter32, iso, MibIdentifier, Integer32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "IpAddress")
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
mibBuilder.exportSymbols("CT-FASTPATH-PROTECTED-PORT-MIB", PYSNMP_MODULE_ID=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortEntry=ctAgentSwitchProtectedPortEntry, ctAgentSwitchProtectedPortGroupId=ctAgentSwitchProtectedPortGroupId, ctAgentSwitchConfigGroup=ctAgentSwitchConfigGroup, ctAgentSwitchProtectedPortGroupName=ctAgentSwitchProtectedPortGroupName, ctAgentSwitchProtectedPortPortList=ctAgentSwitchProtectedPortPortList, ctFastPathProtectedPortMIB=ctFastPathProtectedPortMIB, ctAgentSwitchProtectedPortTable=ctAgentSwitchProtectedPortTable, ctAgentSwitchProtectedPortConfigGroup=ctAgentSwitchProtectedPortConfigGroup)
