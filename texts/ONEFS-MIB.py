#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.8 at Mon Jan 16 15:04:15 2023
# On host fv-az587-63 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Counter64, TimeTicks, Unsigned32, snmpModules, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, NotificationType, Integer32, ObjectIdentity, ModuleIdentity, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "TimeTicks", "Unsigned32", "snmpModules", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "NotificationType", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter32", "enterprises")
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

mibBuilder.exportSymbols("ONEFS-MIB", onefs=onefs, TimeTicks64=TimeTicks64, PYSNMP_MODULE_ID=onefs)
