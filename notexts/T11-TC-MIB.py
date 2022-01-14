#
# PySNMP MIB module T11-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-TC-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:32:29 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Counter32, MibIdentifier, Integer32, IpAddress, NotificationType, ObjectIdentity, mib_2, ModuleIdentity, Gauge32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "ObjectIdentity", "mib-2", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11TcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 136))
t11TcMIB.setRevisions(('2006-03-02 00:00',))
if mibBuilder.loadTexts: t11TcMIB.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: t11TcMIB.setOrganization('T11')
class T11FabricIndex(TextualConvention, Unsigned32):
    reference = 'Fibre Channel - Switch Fabric - 4 (FC-SW-4), ANSI INCITS 418-2006, section 6.1.27.2.4.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

mibBuilder.exportSymbols("T11-TC-MIB", t11TcMIB=t11TcMIB, T11FabricIndex=T11FabricIndex, PYSNMP_MODULE_ID=t11TcMIB)
