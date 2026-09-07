#
# PySNMP MIB module DLINKSW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-TC-MIB
# Source digest sha256:dbcd6bb235398f77ab11747716550e1280a4a647ecec56411847a61966a364e2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwTextualConvention = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 1))
dlinkSwTextualConvention.setRevisions(('2012-11-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwTextualConvention.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: dlinkSwTextualConvention.setLastUpdated('2012-11-19 00:00')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setDescription('The module defines textual conventions used for all proprietary\n             MIBs.')
class DlinkTrigger(TextualConvention, Integer32):
    description = "The object defined by this textual convention can trigger an event.\n             It always returns 'none(1)' when read the object."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("action", 2))

class Dlink2kVlanList(TextualConvention, OctetString):
    description = "This textual convention can specify a VLAN range of 2k VLANs, \n            for example, 1 - 2048, 2049 - 4095, etc. Each octet within this value\n            specifies a set of eight VLANs. The first octet specifies first 8 \n            VLANs of the range specified in the description, the second octet\n            specifies the next 8 VLANs, etc.\n            Within each octet, the most significant bit represents the lowest\n            numbered VLAN, and the least significant bit represents the highest\n            numbered VLAN.  Thus, each VLAN of the device is represented by a\n            single bit within the value of this object. If the corresponding bit\n            is '1' indicates that VLAN is included in the set of VLANs; \n            '0' means the VLAN is not included.\n            Note that if the length of this object is less than 256 octets,\n            any 'missing' octets are assumed to contain the value zero."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mibBuilder.exportSymbols("DLINKSW-TC-MIB", Dlink2kVlanList=Dlink2kVlanList, DlinkTrigger=DlinkTrigger, PYSNMP_MODULE_ID=dlinkSwTextualConvention, dlinkSwTextualConvention=dlinkSwTextualConvention)
