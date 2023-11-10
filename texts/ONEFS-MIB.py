#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 11:11:13 2023
# On host fv-az1251-57 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, snmpModules, Counter64, TimeTicks, Counter32, Integer32, ModuleIdentity, Gauge32, enterprises, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "snmpModules", "Counter64", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "Gauge32", "enterprises", "Unsigned32", "IpAddress")
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
