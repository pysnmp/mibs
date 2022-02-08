#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:31:07 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, enterprises, TimeTicks, iso, Bits, Integer32, Gauge32, Counter32, IpAddress, Counter64, snmpModules, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "enterprises", "TimeTicks", "iso", "Bits", "Integer32", "Gauge32", "Counter32", "IpAddress", "Counter64", "snmpModules", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
onefs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124))
if mibBuilder.loadTexts: onefs.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: onefs.setOrganization('COMPANY_NAME')
if mibBuilder.loadTexts: onefs.setContactInfo('COMPANY_NAME\n\t\t Support phone: SUPPORT_PHONE\n\t\t Support email: SUPPORT_EMAIL\n\t\t')
if mibBuilder.loadTexts: onefs.setDescription('This is the enterprise number for OneFS')
class TimeTicks64(TextualConvention, Counter64):
    description = 'A 64 bit value representing milliseconds from the epoch'
    status = 'current'
    subtypeSpec = Counter64.subtypeSpec + ValueRangeConstraint(0, 18446744073709551615)

mibBuilder.exportSymbols("ONEFS-MIB", PYSNMP_MODULE_ID=onefs, onefs=onefs, TimeTicks64=TimeTicks64)
