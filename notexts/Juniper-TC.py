#
# PySNMP MIB module Juniper-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/Juniper-TC
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:21 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, Integer32, Unsigned32, Bits, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "Integer32", "Unsigned32", "Bits", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 1))
juniTextualConventions.setRevisions(('2005-12-21 20:13', '2005-11-18 22:30', '2004-12-03 22:12', '2003-11-12 22:31', '2002-09-16 21:44', '2002-04-04 16:35', '2001-03-08 22:26', '1999-12-12 00:00', '1999-07-14 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: juniTextualConventions.setLastUpdated('200512212013Z')
if mibBuilder.loadTexts: juniTextualConventions.setOrganization('Juniper Networks, Inc.')
class JuniEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class JuniName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JuniVrfName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniNextIfIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JuniIpAddrLessIf(TextualConvention, IpAddress):
    status = 'current'

class JuniTimeSlotMap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class JuniAcctngAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class JuniAcctngOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("notSupported", 2))

class JuniLogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("off", -1), ("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class JuniSetMap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceDescrFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("proprietary", 0), ("industryCommon", 1))

class JuniInterfaceLocation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slotPort", 1), ("slotAdapterPort", 2), ("adapterPort", 3))

class JuniInterfaceLocationValue(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class JuniVrfGroupName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniTimeFilter(TextualConvention, TimeTicks):
    reference = 'Refer to RFC 2021 for the definition of the TimeFilter, its usage and implementation notes.'
    status = 'current'

class JuniNibbleConfig(TextualConvention, Integer32):
    status = 'current'

mibBuilder.exportSymbols("Juniper-TC", JuniNibbleConfig=JuniNibbleConfig, juniTextualConventions=juniTextualConventions, JuniInterfaceLocation=JuniInterfaceLocation, PYSNMP_MODULE_ID=juniTextualConventions, JuniTimeFilter=JuniTimeFilter, JuniVrfName=JuniVrfName, JuniName=JuniName, JuniInterfaceLocationValue=JuniInterfaceLocationValue, JuniEnable=JuniEnable, JuniAcctngOperType=JuniAcctngOperType, JuniInterfaceLocationType=JuniInterfaceLocationType, JuniInterfaceDescrFormat=JuniInterfaceDescrFormat, JuniVrfGroupName=JuniVrfGroupName, JuniTimeSlotMap=JuniTimeSlotMap, JuniIpAddrLessIf=JuniIpAddrLessIf, JuniLogSeverity=JuniLogSeverity, JuniNextIfIndex=JuniNextIfIndex, JuniSetMap=JuniSetMap, JuniAcctngAdminType=JuniAcctngAdminType)
