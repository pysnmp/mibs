#
# PySNMP MIB module IANATn3270eTC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANATn3270eTC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaTn3270eTcMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 61))
ianaTn3270eTcMib.setRevisions(('2000-05-10 00:00', '1999-09-01 10:00',))
if mibBuilder.loadTexts: ianaTn3270eTcMib.setLastUpdated('200005100000Z')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setOrganization('IANA')
class IANATn3270eAddrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2))

class IANATn3270eAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IANATn3270eClientType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 1), ("other", 2), ("ipv4", 3), ("ipv6", 4), ("domainName", 5), ("truncDomainName", 6), ("string", 7), ("certificate", 8), ("userId", 9), ("x509dn", 10))

class IANATn3270Functions(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("transmitBinary", 0), ("timemark", 1), ("endOfRecord", 2), ("terminalType", 3), ("tn3270Regime", 4), ("scsCtlCodes", 5), ("dataStreamCtl", 6), ("responses", 7), ("bindImage", 8), ("sysreq", 9))

class IANATn3270ResourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("terminal", 2), ("printer", 3), ("terminalOrPrinter", 4))

class IANATn3270DeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100))
    namedValues = NamedValues(("ibm3278d2", 1), ("ibm3278d2E", 2), ("ibm3278d3", 3), ("ibm3278d3E", 4), ("ibm3278d4", 5), ("ibm3278d4E", 6), ("ibm3278d5", 7), ("ibm3278d5E", 8), ("ibmDynamic", 9), ("ibm3287d1", 10), ("unknown", 100))

class IANATn3270eLogData(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(6, 2048), )
mibBuilder.exportSymbols("IANATn3270eTC-MIB", PYSNMP_MODULE_ID=ianaTn3270eTcMib, IANATn3270DeviceType=IANATn3270DeviceType, IANATn3270eLogData=IANATn3270eLogData, IANATn3270eClientType=IANATn3270eClientType, IANATn3270eAddress=IANATn3270eAddress, IANATn3270ResourceType=IANATn3270ResourceType, IANATn3270Functions=IANATn3270Functions, ianaTn3270eTcMib=ianaTn3270eTcMib, IANATn3270eAddrType=IANATn3270eAddrType)
