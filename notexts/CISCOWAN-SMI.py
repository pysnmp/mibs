#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/CISCOWAN-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 05:10:46 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, IpAddress, Integer32, ModuleIdentity, NotificationType, ObjectIdentity, Gauge32, TimeTicks, Counter64, Bits, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "IpAddress", "Integer32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Gauge32", "TimeTicks", "Counter64", "Bits", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('200205240000Z')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
mibBuilder.exportSymbols("CISCOWAN-SMI", ciscoWanAgentCapability=ciscoWanAgentCapability, ciscoWan=ciscoWan, stratacom=stratacom, PYSNMP_MODULE_ID=stratacom)
