#
# PySNMP MIB module PRVT-STORM-CTL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-STORM-CTL-MIB
# Produced by pysmi-1.1.8 at Fri Jan 14 00:09:29 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, Unsigned32, NotificationType, Bits, ModuleIdentity, Integer32, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Unsigned32", "NotificationType", "Bits", "ModuleIdentity", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
prvtStormCtlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 171))
prvtStormCtlMIB.setRevisions(('2010-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtStormCtlMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: prvtStormCtlMIB.setLastUpdated('201006210000Z')
if mibBuilder.loadTexts: prvtStormCtlMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtStormCtlMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtStormCtlMIB.setDescription('The MIB module for managing storm control.')
class RateThresholdType(TextualConvention, Unsigned32):
    description = 'A rate threshold in packets per seconds.'
    status = 'current'
    displayHint = 'd'

prvtStormCtlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1))
prvtStrmCtlPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1), )
if mibBuilder.loadTexts: prvtStrmCtlPortTable.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTable.setDescription('A list of interfaces that have storm control functionality configured.')
prvtStrmCtlPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtStrmCtlPortEntry.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortEntry.setDescription('An entry in prvtStrmCtlPortTable.')
prvtStrmCtlPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortRowStatus.setDescription('The RowStatus for this port.')
prvtStrmCtlPortShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortShutdown.setDescription("Set to 'false' to enable storm control functionality on this port.")
prvtStrmCtlPortTrafficTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3), )
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficTable.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficTable.setDescription('A table of traffic-type specific configuration for each interface.\n         Currently, only one traffic type is supported per interface.')
prvtStrmCtlPortTrafficEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-STORM-CTL-MIB", "prvtStrmCtlPortTrafficType"))
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficEntry.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficEntry.setDescription('An entry in prvtStrmCtlPortTrafficTable.')
prvtStrmCtlPortTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("all", 0), ("unknown", 1), ("multicast", 2), ("broadcast", 4))))
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficType.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficType.setDescription('The type of traffic to which this row applies ')
prvtStrmCtlPortTrafficRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficRowStatus.setDescription('The RowStatus for this traffic type.')
prvtStrmCtlPortTrafficThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 3), RateThresholdType()).setUnits('packets-per-second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficThreshold.setDescription('The threshold at which, when exceeded, traffic will undergo\n         storm control action for this port and traffic type.')
mibBuilder.exportSymbols("PRVT-STORM-CTL-MIB", prvtStrmCtlPortEntry=prvtStrmCtlPortEntry, prvtStrmCtlPortRowStatus=prvtStrmCtlPortRowStatus, prvtStrmCtlPortTrafficEntry=prvtStrmCtlPortTrafficEntry, prvtStrmCtlPortShutdown=prvtStrmCtlPortShutdown, PYSNMP_MODULE_ID=prvtStormCtlMIB, prvtStormCtlMIBObjects=prvtStormCtlMIBObjects, prvtStormCtlMIB=prvtStormCtlMIB, prvtStrmCtlPortTrafficRowStatus=prvtStrmCtlPortTrafficRowStatus, prvtStrmCtlPortTrafficThreshold=prvtStrmCtlPortTrafficThreshold, prvtStrmCtlPortTrafficType=prvtStrmCtlPortTrafficType, RateThresholdType=RateThresholdType, prvtStrmCtlPortTable=prvtStrmCtlPortTable, prvtStrmCtlPortTrafficTable=prvtStrmCtlPortTrafficTable)
