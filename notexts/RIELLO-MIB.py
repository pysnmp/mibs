#
# PySNMP MIB module RIELLO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source RIELLO-MIB
# Source digest sha256:452fa1daac9fa7938096f6019453403b894c6782c65f8cf79a3e061db2ee5838
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rielloMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5491))
rielloMIB.setRevisions(('2016-02-23 00:00',))
if mibBuilder.loadTexts: rielloMIB.setLastUpdated('2016-02-23 00:00')
if mibBuilder.loadTexts: rielloMIB.setOrganization('RPS S.p.A')
mibBuilder.exportSymbols("RIELLO-MIB", PYSNMP_MODULE_ID=rielloMIB, rielloMIB=rielloMIB)
