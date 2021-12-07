#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 17:31:39 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, Counter32, Unsigned32, Gauge32, TimeTicks, IpAddress, MibIdentifier, iso, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Counter32", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
if mibBuilder.loadTexts: sagemDr.setContactInfo('    ')
if mibBuilder.loadTexts: sagemDr.setDescription('The MIB module defines enterprises/sagem-r entry')
mibBuilder.exportSymbols("SAGEM-DR-MIB", PYSNMP_MODULE_ID=sagemDr, sagemDr=sagemDr)
