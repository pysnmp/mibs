#
# PySNMP MIB module LANTRONIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lantronix/LANTRONIX-MIB.mib
# Produced by pysmi-1.1.12 at Fri Apr 12 00:30:32 2024
# On host fv-az975-788 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, Gauge32, Unsigned32, enterprises, NotificationType, IpAddress, Counter32, Bits, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "Unsigned32", "enterprises", "NotificationType", "IpAddress", "Counter32", "Bits", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lantronix = ModuleIdentity((1, 3, 6, 1, 4, 1, 244))
lantronix.setRevisions(('2007-03-01 00:00', '2006-11-10 00:00', '2004-12-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lantronix.setRevisionsDescriptions(('Added legacy products.', 'Added sls product.', 'The initial version of the MIB module.',))
if mibBuilder.loadTexts: lantronix.setLastUpdated('200703010000Z')
if mibBuilder.loadTexts: lantronix.setOrganization('Lantronix, Inc.')
if mibBuilder.loadTexts: lantronix.setContactInfo('Lantronix Technical Support\n                  15353 Barranca Parkway\n                  Irvine, CA 92618 USA\n                  +1 800 422-7044\n                  snmp@lantronix.com')
if mibBuilder.loadTexts: lantronix.setDescription('The structure of Management Information for the Lantronix enterprise')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1))
slc = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 1))
slk = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 8))
slp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9))
slm = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 10))
sls = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 11))
ltxlna = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 10))
ltxlrp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 11))
ltxlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 12))
mibBuilder.exportSymbols("LANTRONIX-MIB", slc=slc, slk=slk, products=products, lantronix=lantronix, PYSNMP_MODULE_ID=lantronix, slm=slm, ltxlna=ltxlna, ltxlrp=ltxlrp, sls=sls, ltxlsw=ltxlsw, slp=slp)
