#
# PySNMP MIB module CISCO-TRUSTSEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-TC-MIB
# Source digest sha256:bd75c81c392193dea412135dc7c55546094aaeb9a0b4c68ed7f00fbf352cb598
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCtsTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 694))
ciscoCtsTcMIB.setRevisions(('2013-06-06 00:00', '2012-01-30 00:00', '2009-05-14 00:00',))
if mibBuilder.loadTexts: ciscoCtsTcMIB.setLastUpdated('2013-06-06 00:00')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setOrganization('Cisco Systems, Inc.')
class CtsSecurityGroupTag(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CtsAclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsAclList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclListOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPolicyName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPasswordEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("clearText", 3), ("typeSix", 4), ("typeSeven", 5))

class CtsPassword(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CtsGenerationId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CtsAcsAuthorityIdentity(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CtsCredentialRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("simpleSecret", 1), ("pac", 2))

class CtsSgaclMonitorMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class CtsSxpConnectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("off", 2), ("on", 3), ("pendingOn", 4), ("deleteHoldDown", 5))

mibBuilder.exportSymbols("CISCO-TRUSTSEC-TC-MIB", CtsAclList=CtsAclList, CtsAclListOrEmpty=CtsAclListOrEmpty, CtsAclName=CtsAclName, CtsAclNameOrEmpty=CtsAclNameOrEmpty, CtsAcsAuthorityIdentity=CtsAcsAuthorityIdentity, CtsCredentialRecordType=CtsCredentialRecordType, CtsGenerationId=CtsGenerationId, CtsPassword=CtsPassword, CtsPasswordEncryptionType=CtsPasswordEncryptionType, CtsPolicyName=CtsPolicyName, CtsSecurityGroupTag=CtsSecurityGroupTag, CtsSgaclMonitorMode=CtsSgaclMonitorMode, CtsSxpConnectionStatus=CtsSxpConnectionStatus, PYSNMP_MODULE_ID=ciscoCtsTcMIB, ciscoCtsTcMIB=ciscoCtsTcMIB)
