#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/CISCOWAN-SMI
# Produced by pysmi-1.1.8 at Thu Jan 13 23:32:41 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Counter32, enterprises, IpAddress, Bits, MibIdentifier, Counter64, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Counter32", "enterprises", "IpAddress", "Bits", "MibIdentifier", "Counter64", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('200205240000Z')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
mibBuilder.exportSymbols("CISCOWAN-SMI", PYSNMP_MODULE_ID=stratacom, ciscoWan=ciscoWan, ciscoWanAgentCapability=ciscoWanAgentCapability, stratacom=stratacom)
