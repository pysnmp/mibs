#
# PySNMP MIB module T11-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source T11-TC-MIB
# Source digest sha256:290e911fd81cad3224ea28616c4cdae67844b61a11eb9a6da9ee10ef45ec0c27
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11TcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 136))
t11TcMIB.setRevisions(('2006-03-02 00:00',))
if mibBuilder.loadTexts: t11TcMIB.setLastUpdated('2006-03-02 00:00')
if mibBuilder.loadTexts: t11TcMIB.setOrganization('T11')
class T11FabricIndex(TextualConvention, Unsigned32):
    reference = 'Fibre Channel - Switch Fabric - 4 (FC-SW-4), ANSI INCITS 418-2006, section 6.1.27.2.4.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

mibBuilder.exportSymbols("T11-TC-MIB", PYSNMP_MODULE_ID=t11TcMIB, T11FabricIndex=T11FabricIndex, t11TcMIB=t11TcMIB)
