#
# PySNMP MIB module CTRON-BUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-BUS-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:05:29 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ctAtmfLanEmulation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctAtmfLanEmulation")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, TimeTicks, MibIdentifier, ModuleIdentity, IpAddress, Bits, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "TimeTicks", "MibIdentifier", "ModuleIdentity", "IpAddress", "Bits", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctBus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4))
ctBusConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1))
class CtLaneDebugLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("user", 1), ("all", 2), ("error", 3), ("warning", 4), ("informational", 5), ("detailed", 6), ("trace", 7))

ctBusDSStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connected", 1), ("connectionLost", 2), ("unknown", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBusDSStatus.setStatus('mandatory')
ctBusUNIVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("uni30", 2), ("uni31", 3), ("uni40", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBusUNIVersion.setStatus('mandatory')
ctBusLaneDbgOutputFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgOutputFile.setStatus('mandatory')
ctBusLaneDbgConnectionServices = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 4), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgConnectionServices.setStatus('mandatory')
ctBusLaneDbgSNMP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 5), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgSNMP.setStatus('mandatory')
ctBusLaneDbgBUS = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 6), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgBUS.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-BUS-MIB", ctBusDSStatus=ctBusDSStatus, CtLaneDebugLevel=CtLaneDebugLevel, ctBusLaneDbgBUS=ctBusLaneDbgBUS, ctBus=ctBus, ctBusLaneDbgConnectionServices=ctBusLaneDbgConnectionServices, ctBusLaneDbgOutputFile=ctBusLaneDbgOutputFile, ctBusConfGroup=ctBusConfGroup, ctBusLaneDbgSNMP=ctBusLaneDbgSNMP, ctBusUNIVersion=ctBusUNIVersion)
