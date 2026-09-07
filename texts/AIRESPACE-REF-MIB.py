#
# PySNMP MIB module AIRESPACE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source AIRESPACE-REF-MIB
# Source digest sha256:2695cf8276581bc1697283e5584942bf5ad3972286c42db36899fbaf7048ef96
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
airespace = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179))
airespace.setRevisions(('2005-12-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: airespace.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: airespace.setLastUpdated('2005-12-19 00:00')
if mibBuilder.loadTexts: airespace.setOrganization('Airespace, Inc.')
if mibBuilder.loadTexts: airespace.setContactInfo('        Cisco Systems,\n                     Customer Service\n             Postal: 170 West Tasman Drive\n                     San Jose, CA  95134\n                     USA\n                Tel: +1 800 553-NETS\n\n              Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: airespace.setDescription('The Structure of Management Information for the\n             Airespace enterprise.')
mibBuilder.exportSymbols("AIRESPACE-REF-MIB", PYSNMP_MODULE_ID=airespace, airespace=airespace)
