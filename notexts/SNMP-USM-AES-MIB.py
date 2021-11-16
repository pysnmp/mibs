#
# PySNMP MIB module SNMP-USM-AES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-USM-AES-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:26:57 2021
# On host fv-az77-509 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
snmpPrivProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, snmpModules, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ObjectIdentity, MibIdentifier, iso, IpAddress, Unsigned32, Bits, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "snmpModules", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "IpAddress", "Unsigned32", "Bits", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmAesMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 20))
snmpUsmAesMIB.setRevisions(('2004-06-14 00:00',))
if mibBuilder.loadTexts: snmpUsmAesMIB.setLastUpdated('200406140000Z')
if mibBuilder.loadTexts: snmpUsmAesMIB.setOrganization('IETF')
usmAesCfb128Protocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
if mibBuilder.loadTexts: usmAesCfb128Protocol.setStatus('current')
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", PYSNMP_MODULE_ID=snmpUsmAesMIB, snmpUsmAesMIB=snmpUsmAesMIB, usmAesCfb128Protocol=usmAesCfb128Protocol)
