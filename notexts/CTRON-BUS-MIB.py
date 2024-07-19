#
# PySNMP MIB module CTRON-BUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-BUS-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 11:35:16 2024
# On host fv-az702-886 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ctAtmfLanEmulation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctAtmfLanEmulation")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, Counter32, Integer32, Counter64, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "Counter32", "Integer32", "Counter64", "IpAddress", "ModuleIdentity")
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
mibBuilder.exportSymbols("CTRON-BUS-MIB", ctBus=ctBus, ctBusUNIVersion=ctBusUNIVersion, ctBusDSStatus=ctBusDSStatus, ctBusLaneDbgBUS=ctBusLaneDbgBUS, ctBusLaneDbgSNMP=ctBusLaneDbgSNMP, CtLaneDebugLevel=CtLaneDebugLevel, ctBusLaneDbgConnectionServices=ctBusLaneDbgConnectionServices, ctBusConfGroup=ctBusConfGroup, ctBusLaneDbgOutputFile=ctBusLaneDbgOutputFile)
