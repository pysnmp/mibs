#
# PySNMP MIB module SNMP-USM-AES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-USM-AES-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 15:06:48 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
snmpPrivProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, NotificationType, Bits, iso, ObjectIdentity, TimeTicks, Gauge32, IpAddress, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, snmpModules, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Bits", "iso", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "snmpModules", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmAesMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 20))
snmpUsmAesMIB.setRevisions(('2004-06-14 00:00',))
if mibBuilder.loadTexts: snmpUsmAesMIB.setLastUpdated('200406140000Z')
if mibBuilder.loadTexts: snmpUsmAesMIB.setOrganization('IETF')
usmAesCfb128Protocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
if mibBuilder.loadTexts: usmAesCfb128Protocol.setStatus('current')
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", snmpUsmAesMIB=snmpUsmAesMIB, usmAesCfb128Protocol=usmAesCfb128Protocol, PYSNMP_MODULE_ID=snmpUsmAesMIB)
