#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:21:33 2024
# On host fv-az1984-402 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
snmpModules, MibIdentifier, Bits, IpAddress, TimeTicks, ModuleIdentity, enterprises, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity, iso, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "snmpModules", "MibIdentifier", "Bits", "IpAddress", "TimeTicks", "ModuleIdentity", "enterprises", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity", "iso", "Integer32", "NotificationType")
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

mibBuilder.exportSymbols("ONEFS-MIB", TimeTicks64=TimeTicks64, onefs=onefs, PYSNMP_MODULE_ID=onefs)
