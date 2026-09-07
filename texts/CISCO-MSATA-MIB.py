#
# PySNMP MIB module CISCO-MSATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MSATA-MIB
# Source digest sha256:5ba338aa28e11000ac223cd97e3bb8150fd9bd116674395eb2a85b2a32abdfdf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMsataMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 860))
ciscoMsataMIB.setRevisions(('2019-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMsataMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMsataMIB.setLastUpdated('2019-01-09 00:00')
if mibBuilder.loadTexts: ciscoMsataMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMsataMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ir800@cisco.com')
if mibBuilder.loadTexts: ciscoMsataMIB.setDescription('As part of this enhancement, adding SNMP support for below 2\n        mSata parameters on the IR829M products:\n        1) Lifetime remaining (wear leveling)\n        2) Memory usage for the mSATA SSD\n\n        This feature is supported in IR829M only.\n\n        *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS ***\n\n        Wl      -   Wear Leveling of mSATA SSD')
ciscoMsataMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 860, 0))
ciscoMsata = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 860, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMsata.setStatus('current')
if mibBuilder.loadTexts: ciscoMsata.setDescription('An entry containing the management information for a mSata\n        parameters - Lifetime remaining and memory usage.')
mibBuilder.exportSymbols("CISCO-MSATA-MIB", PYSNMP_MODULE_ID=ciscoMsataMIB, ciscoMsata=ciscoMsata, ciscoMsataMIB=ciscoMsataMIB, ciscoMsataMIBObjects=ciscoMsataMIBObjects)
