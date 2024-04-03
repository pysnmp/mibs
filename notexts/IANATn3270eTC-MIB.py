#
# PySNMP MIB module IANATn3270eTC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANATn3270eTC-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 14:46:39 2024
# On host fv-az1198-695 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Counter32, Unsigned32, MibIdentifier, IpAddress, ModuleIdentity, Gauge32, NotificationType, Integer32, mib_2, ObjectIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Gauge32", "NotificationType", "Integer32", "mib-2", "ObjectIdentity", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("IANATn3270eTC-MIB", IANATn3270eLogData=IANATn3270eLogData, ianaTn3270eTcMib=ianaTn3270eTcMib, IANATn3270Functions=IANATn3270Functions, IANATn3270ResourceType=IANATn3270ResourceType, IANATn3270eAddrType=IANATn3270eAddrType, IANATn3270eAddress=IANATn3270eAddress, PYSNMP_MODULE_ID=ianaTn3270eTcMib, IANATn3270DeviceType=IANATn3270DeviceType, IANATn3270eClientType=IANATn3270eClientType)
