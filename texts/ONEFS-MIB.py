#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:52:48 2024
# On host fv-az2028-26 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, Unsigned32, ObjectIdentity, iso, snmpModules, NotificationType, Counter32, enterprises, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "Unsigned32", "ObjectIdentity", "iso", "snmpModules", "NotificationType", "Counter32", "enterprises", "Integer32", "ModuleIdentity")
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

mibBuilder.exportSymbols("ONEFS-MIB", PYSNMP_MODULE_ID=onefs, TimeTicks64=TimeTicks64, onefs=onefs)
