#
# PySNMP MIB module CISCO-DMN-DSG-DECODE-ENABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DMN-DSG-DECODE-ENABLE-MIB
# Source digest sha256:5ea98b28be23bfc16924c9e43e0d4eb1d82400ded69f23114d0b28f40e0092fa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGDecodeEnable = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13))
ciscoDSGDecodeEnable.setRevisions(('2010-08-30 06:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setRevisionsDescriptions(('V01.00.01 2010-08-30\n                   Update for adherence to SNMPv2 format.', 'V01.00.00 2009-12-07\n                   Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setLastUpdated('2010-08-30 06:00')
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setContactInfo('Cisco Systems, Inc.\n        Customer Service \n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA  \n        Tel: +1 800 553 NETS\n        \n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setDescription('Cisco Decoder Service Enable MIB.')
decodeEnableTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: decodeEnableTable.setStatus('current')
if mibBuilder.loadTexts: decodeEnableTable.setDescription('Decode Service Enable Table.')
decodeEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DMN-DSG-DECODE-ENABLE-MIB", "decodeType"))
if mibBuilder.loadTexts: decodeEnableEntry.setStatus('current')
if mibBuilder.loadTexts: decodeEnableEntry.setDescription('Entry for Decoder Service Enable Table.')
decodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("video", 1), ("audio1", 2), ("audio2", 3), ("audio3", 4), ("audio4", 5), ("vbi", 6), ("data", 7), ("mpe1", 8), ("mpe2", 9), ("mpe3", 10), ("mpe4", 11), ("mpe5", 12), ("stt", 13), ("dpi", 14)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: decodeType.setStatus('current')
if mibBuilder.loadTexts: decodeType.setDescription('Decodeable Service type.\n        This field used as a key for setting particular service\n        to be enabled/disbled.')
decodeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: decodeEnable.setStatus('current')
if mibBuilder.loadTexts: decodeEnable.setDescription('Enable or disable the decoder service.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DECODE-ENABLE-MIB", PYSNMP_MODULE_ID=ciscoDSGDecodeEnable, ciscoDSGDecodeEnable=ciscoDSGDecodeEnable, decodeEnable=decodeEnable, decodeEnableEntry=decodeEnableEntry, decodeEnableTable=decodeEnableTable, decodeType=decodeType)
