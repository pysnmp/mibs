#
# PySNMP MIB module IRONPORT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source IRONPORT-SMI
# Source digest sha256:4c467fbd824aecc6b90836ca03fd5414b4ce2ca53f60a92f350f52b7c3668af5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ironPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 15497))
ironPort.setRevisions(('2011-05-02 16:00', '2005-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ironPort.setRevisionsDescriptions(('Cleaned up SMI definition.', 'Initial revision.',))
if mibBuilder.loadTexts: ironPort.setLastUpdated('2011-05-02 16:00')
if mibBuilder.loadTexts: ironPort.setOrganization('IronPort Systems')
if mibBuilder.loadTexts: ironPort.setContactInfo('       Cisco IronPort Email and Web Security\n                Customer Service\n\n        Postal: 950 Elm Avenue\n                San Bruno, CA 94066\n                USA\n\n           Tel: +1 (650) 989-6533\n\n        E-mail: customercare@ironport.com')
if mibBuilder.loadTexts: ironPort.setDescription('Top-level infrastructure of the Cisco IronPort project\n         enterprise MIB tree.')
asyncOSAppliances = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1))
asyncOSMail = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 1))
mibBuilder.exportSymbols("IRONPORT-SMI", PYSNMP_MODULE_ID=ironPort, asyncOSAppliances=asyncOSAppliances, asyncOSMail=asyncOSMail, ironPort=ironPort)
