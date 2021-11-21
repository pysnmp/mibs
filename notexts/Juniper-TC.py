#
# PySNMP MIB module Juniper-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/Juniper-TC
# Produced by pysmi-1.1.3 at Sun Nov 21 13:56:39 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, Counter64, Gauge32, Bits, Counter32, ObjectIdentity, NotificationType, Integer32, ModuleIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Counter64", "Gauge32", "Bits", "Counter32", "ObjectIdentity", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("Juniper-TC", JuniNibbleConfig=JuniNibbleConfig, JuniIpAddrLessIf=JuniIpAddrLessIf, JuniInterfaceLocation=JuniInterfaceLocation, JuniNextIfIndex=JuniNextIfIndex, JuniVrfName=JuniVrfName, JuniAcctngOperType=JuniAcctngOperType, PYSNMP_MODULE_ID=juniTextualConventions, JuniInterfaceLocationValue=JuniInterfaceLocationValue, JuniSetMap=JuniSetMap, JuniVrfGroupName=JuniVrfGroupName, JuniLogSeverity=JuniLogSeverity, JuniInterfaceDescrFormat=JuniInterfaceDescrFormat, JuniInterfaceLocationType=JuniInterfaceLocationType, JuniName=JuniName, juniTextualConventions=juniTextualConventions, JuniAcctngAdminType=JuniAcctngAdminType, JuniTimeFilter=JuniTimeFilter, JuniEnable=JuniEnable, JuniTimeSlotMap=JuniTimeSlotMap)
