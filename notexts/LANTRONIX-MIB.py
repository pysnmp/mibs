#
# PySNMP MIB module LANTRONIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lantronix/LANTRONIX-MIB.mib
# Produced by pysmi-1.1.8 at Thu Jan 13 23:07:59 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, ModuleIdentity, IpAddress, Gauge32, Integer32, MibIdentifier, NotificationType, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "MibIdentifier", "NotificationType", "enterprises", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lantronix = ModuleIdentity((1, 3, 6, 1, 4, 1, 244))
lantronix.setRevisions(('2007-03-01 00:00', '2006-11-10 00:00', '2004-12-13 00:00',))
if mibBuilder.loadTexts: lantronix.setLastUpdated('200703010000Z')
if mibBuilder.loadTexts: lantronix.setOrganization('Lantronix, Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1))
slc = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 1))
slk = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 8))
slp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9))
slm = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 10))
sls = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 11))
ltxlna = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 10))
ltxlrp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 11))
ltxlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 12))
mibBuilder.exportSymbols("LANTRONIX-MIB", ltxlna=ltxlna, ltxlsw=ltxlsw, slp=slp, slc=slc, slk=slk, ltxlrp=ltxlrp, PYSNMP_MODULE_ID=lantronix, slm=slm, sls=sls, products=products, lantronix=lantronix)
