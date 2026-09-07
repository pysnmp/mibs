#
# PySNMP MIB module CISCO-SNMP-USM-OIDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-USM-OIDS-MIB
# Source digest sha256:b3d7854867674b2c5d2abf8dc2ad9468876b272535ce9fb3d5f526e4ae566244
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpUsmOidsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 6))
ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setLastUpdated('2006-02-28 00:00')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1))
cusmAESCfb192PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1))
cusmAESCfb256PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2))
cusm3DES168PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3))
mibBuilder.exportSymbols("CISCO-SNMP-USM-OIDS-MIB", PYSNMP_MODULE_ID=ciscoSnmpUsmOidsMIB, ciscoSnmpPrivProtocols=ciscoSnmpPrivProtocols, ciscoSnmpUsmOidsMIB=ciscoSnmpUsmOidsMIB, cusm3DES168PrivProtocol=cusm3DES168PrivProtocol, cusmAESCfb192PrivProtocol=cusmAESCfb192PrivProtocol, cusmAESCfb256PrivProtocol=cusmAESCfb256PrivProtocol)
