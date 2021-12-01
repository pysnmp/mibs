#
# PySNMP MIB module PRVT-STORM-CTL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-STORM-CTL-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:44:32 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, NotificationType, Unsigned32, MibIdentifier, Counter32, Integer32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
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
mibBuilder.exportSymbols("PRVT-STORM-CTL-MIB", prvtStrmCtlPortShutdown=prvtStrmCtlPortShutdown, RateThresholdType=RateThresholdType, prvtStrmCtlPortTrafficEntry=prvtStrmCtlPortTrafficEntry, prvtStrmCtlPortTrafficRowStatus=prvtStrmCtlPortTrafficRowStatus, prvtStormCtlMIB=prvtStormCtlMIB, prvtStrmCtlPortTable=prvtStrmCtlPortTable, prvtStormCtlMIBObjects=prvtStormCtlMIBObjects, PYSNMP_MODULE_ID=prvtStormCtlMIB, prvtStrmCtlPortEntry=prvtStrmCtlPortEntry, prvtStrmCtlPortRowStatus=prvtStrmCtlPortRowStatus, prvtStrmCtlPortTrafficTable=prvtStrmCtlPortTrafficTable, prvtStrmCtlPortTrafficType=prvtStrmCtlPortTrafficType, prvtStrmCtlPortTrafficThreshold=prvtStrmCtlPortTrafficThreshold)
