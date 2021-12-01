#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 15:40:50 2021
# On host fv-az74-277 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, Counter32, NotificationType, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, iso, TimeTicks, Bits, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "iso", "TimeTicks", "Bits", "Unsigned32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
if mibBuilder.loadTexts: sagemDr.setContactInfo('    ')
if mibBuilder.loadTexts: sagemDr.setDescription('The MIB module defines enterprises/sagem-r entry')
mibBuilder.exportSymbols("SAGEM-DR-MIB", sagemDr=sagemDr, PYSNMP_MODULE_ID=sagemDr)
