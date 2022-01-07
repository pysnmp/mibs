#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/CISCOWAN-SMI
# Produced by pysmi-1.1.8 at Fri Jan  7 17:30:23 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Gauge32, iso, Integer32, NotificationType, Counter64, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Gauge32", "iso", "Integer32", "NotificationType", "Counter64", "IpAddress", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('200205240000Z')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
mibBuilder.exportSymbols("CISCOWAN-SMI", PYSNMP_MODULE_ID=stratacom, ciscoWan=ciscoWan, ciscoWanAgentCapability=ciscoWanAgentCapability, stratacom=stratacom)
