#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:05:33 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, IpAddress, MibIdentifier, TimeTicks, NotificationType, Unsigned32, ModuleIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "IpAddress", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
if mibBuilder.loadTexts: sagemDr.setContactInfo('    ')
if mibBuilder.loadTexts: sagemDr.setDescription('The MIB module defines enterprises/sagem-r entry')
mibBuilder.exportSymbols("SAGEM-DR-MIB", sagemDr=sagemDr, PYSNMP_MODULE_ID=sagemDr)
