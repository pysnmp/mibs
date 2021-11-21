#
# PySNMP MIB module PRVT-STORM-CTL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-STORM-CTL-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:56:12 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Unsigned32, ObjectIdentity, TimeTicks, IpAddress, Integer32, Gauge32, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Unsigned32", "ObjectIdentity", "TimeTicks", "IpAddress", "Integer32", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
prvtStormCtlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 171))
prvtStormCtlMIB.setRevisions(('2010-06-21 00:00',))
if mibBuilder.loadTexts: prvtStormCtlMIB.setLastUpdated('201006210000Z')
if mibBuilder.loadTexts: prvtStormCtlMIB.setOrganization('BATM Advanced Communication')
class RateThresholdType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

prvtStormCtlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1))
prvtStrmCtlPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1), )
if mibBuilder.loadTexts: prvtStrmCtlPortTable.setStatus('current')
prvtStrmCtlPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtStrmCtlPortEntry.setStatus('current')
prvtStrmCtlPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortRowStatus.setStatus('current')
prvtStrmCtlPortShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortShutdown.setStatus('current')
prvtStrmCtlPortTrafficTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3), )
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficTable.setStatus('current')
prvtStrmCtlPortTrafficEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-STORM-CTL-MIB", "prvtStrmCtlPortTrafficType"))
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficEntry.setStatus('current')
prvtStrmCtlPortTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("all", 0), ("unknown", 1), ("multicast", 2), ("broadcast", 4))))
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficType.setStatus('current')
prvtStrmCtlPortTrafficRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficRowStatus.setStatus('current')
prvtStrmCtlPortTrafficThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 171, 1, 3, 1, 3), RateThresholdType()).setUnits('packets-per-second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStrmCtlPortTrafficThreshold.setStatus('current')
mibBuilder.exportSymbols("PRVT-STORM-CTL-MIB", prvtStrmCtlPortTrafficEntry=prvtStrmCtlPortTrafficEntry, prvtStrmCtlPortTrafficTable=prvtStrmCtlPortTrafficTable, prvtStormCtlMIB=prvtStormCtlMIB, prvtStormCtlMIBObjects=prvtStormCtlMIBObjects, prvtStrmCtlPortShutdown=prvtStrmCtlPortShutdown, prvtStrmCtlPortTrafficType=prvtStrmCtlPortTrafficType, PYSNMP_MODULE_ID=prvtStormCtlMIB, prvtStrmCtlPortTable=prvtStrmCtlPortTable, prvtStrmCtlPortTrafficThreshold=prvtStrmCtlPortTrafficThreshold, prvtStrmCtlPortEntry=prvtStrmCtlPortEntry, RateThresholdType=RateThresholdType, prvtStrmCtlPortTrafficRowStatus=prvtStrmCtlPortTrafficRowStatus, prvtStrmCtlPortRowStatus=prvtStrmCtlPortRowStatus)
