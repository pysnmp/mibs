#
# PySNMP MIB module CTRON-BUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-BUS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:25:58 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ctAtmfLanEmulation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctAtmfLanEmulation")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, IpAddress, Bits, TimeTicks, Counter32, Counter64, Gauge32, ModuleIdentity, Unsigned32, iso, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "IpAddress", "Bits", "TimeTicks", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctBus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4))
ctBusConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1))
class CtLaneDebugLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("user", 1), ("all", 2), ("error", 3), ("warning", 4), ("informational", 5), ("detailed", 6), ("trace", 7))

ctBusDSStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connected", 1), ("connectionLost", 2), ("unknown", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBusDSStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusDSStatus.setDescription('Reports the current status of the Secure Fast Directory\n         Services connection.')
ctBusUNIVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("uni30", 2), ("uni31", 3), ("uni40", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBusUNIVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusUNIVersion.setDescription('Reports the UNI version that the bus is using.')
ctBusLaneDbgOutputFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgOutputFile.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusLaneDbgOutputFile.setDescription('Full path and file for Debug Output.')
ctBusLaneDbgConnectionServices = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 4), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgConnectionServices.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusLaneDbgConnectionServices.setDescription('Debug level specifier for Connection Services subsystem.')
ctBusLaneDbgSNMP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 5), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgSNMP.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusLaneDbgSNMP.setDescription('Debug level specifier for SNMP Agent subsystem.')
ctBusLaneDbgBUS = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 6), CtLaneDebugLevel().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBusLaneDbgBUS.setStatus('mandatory')
if mibBuilder.loadTexts: ctBusLaneDbgBUS.setDescription('Debug level specifier for BUS subsystem.')
mibBuilder.exportSymbols("CTRON-BUS-MIB", ctBusConfGroup=ctBusConfGroup, ctBusUNIVersion=ctBusUNIVersion, ctBusDSStatus=ctBusDSStatus, ctBusLaneDbgConnectionServices=ctBusLaneDbgConnectionServices, CtLaneDebugLevel=CtLaneDebugLevel, ctBusLaneDbgBUS=ctBusLaneDbgBUS, ctBus=ctBus, ctBusLaneDbgSNMP=ctBusLaneDbgSNMP, ctBusLaneDbgOutputFile=ctBusLaneDbgOutputFile)
